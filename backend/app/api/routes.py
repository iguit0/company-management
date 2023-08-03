import json

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.api.utils.db import load_companies_from_file, save_companies_to_file
from app.models.schemas import CompanySchema, CompanyUpdateSchema

api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/companies", methods=["GET"])
def list_companies():
    """List all companies"""
    current_companies = load_companies_from_file()
    start = int(request.args.get("start", 0))
    limit = int(request.args.get("limit", 10))
    sort = request.args.get("sort", "cnpj")
    direction = request.args.get("dir", "asc")

    companies_sorted = sorted(
        current_companies,
        key=lambda company: company[sort],
        reverse=direction.lower() == "desc",
    )
    companies_paginated = companies_sorted[start : start + limit]

    return jsonify(companies_paginated)


@api_bp.route("/companies", methods=["POST"])
def create_company():
    """Create a new company"""
    data = request.get_json()

    schema = CompanySchema()

    try:
        company_data = schema.load(data)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid payload."}), 400
    except ValidationError as err:
        return jsonify(err.messages), 400

    current_companies = load_companies_from_file()

    for company in current_companies:
        if company["cnpj"] == company_data["cnpj"]:
            return (
                jsonify(
                    {"error": "Company with the same CNPJ already exists."}
                ),
                409,
            )

    current_companies.append(company_data)
    save_companies_to_file(current_companies)
    return jsonify({"message": "Company successfully registered!"})


@api_bp.route("/companies/<cnpj>", methods=["PUT"])
def update_company(cnpj: str):
    """Update a company by CNPJ"""
    current_companies = load_companies_from_file()
    data = request.get_json()

    schema = CompanyUpdateSchema()
    try:
        validated_data = schema.load(data)
    except Exception as exc_err:
        return jsonify({"error": str(exc_err)}), 400

    updated = False
    for company in current_companies:
        if str(company["cnpj"]) == cnpj:
            company["trading_name"] = validated_data["trading_name"]
            company["company_name"] = validated_data["company_name"]
            company["cnae"] = validated_data["cnae"]
            updated = True
            break

    if updated:
        save_companies_to_file(current_companies)
        return (
            jsonify(
                {
                    "message": "Company updated successfully!",
                    "updated_company": validated_data,
                }
            ),
            200,
        )

    return jsonify({"error": "Company not found."}), 404


@api_bp.route("/companies/<cnpj>", methods=["DELETE"])
def delete_company(cnpj: str):
    """Delete a company by CNPJ"""
    current_companies = load_companies_from_file()

    index_to_remove = None
    for idx, company in enumerate(current_companies):
        if str(company["cnpj"]) == cnpj:
            index_to_remove = idx
            break

    if index_to_remove is not None:
        current_companies.pop(index_to_remove)

        save_companies_to_file(current_companies)

        return jsonify({"message": "Company deleted successfully!"}), 200

    return jsonify({"error": "Company not found."}), 404
