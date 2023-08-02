import json

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.api.utils.db import load_companies_from_file, save_companies_to_file
from app.models.schemas import CompanySchema

api_bp = Blueprint("api_bp", __name__)

companies = load_companies_from_file()


@api_bp.route("/companies", methods=["POST"])
def create_company():
    data = request.get_json()

    schema = CompanySchema()

    try:
        # Validate the request data against the schema
        company_data = schema.load(data)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid payload."}), 400
    except ValidationError as err:
        return jsonify(err.messages), 400

    for company in companies:
        if company["cnpj"] == company_data["cnpj"]:
            return (
                jsonify(
                    {"error": "Company with the same CNPJ already exists."}
                ),
                409,
            )

    companies.append(company_data)
    save_companies_to_file(companies)
    return jsonify({"message": "Company successfully registered!"})


@api_bp.route("/companies/<cnpj>", methods=["PUT"])
def update_company(cnpj):
    data = request.get_json()
    for company in companies:
        if company["cnpj"] == cnpj:
            company["Nome Fantasia"] = data["Nome Fantasia"]
            company["CNAE"] = data["CNAE"]
            save_companies_to_file(companies)
            return jsonify({"message": "Company updated successfully!"})
    return jsonify({"error": "Company not found."}), 404


@api_bp.route("/companies/<cnpj>", methods=["DELETE"])
def delete_company(cnpj):
    global companies
    companies = [company for company in companies if company["cnpj"] != cnpj]
    save_companies_to_file(companies)
    return jsonify({"message": "Company deleted successfully!"})


@api_bp.route("/companies", methods=["GET"])
def list_companies():
    start = int(request.args.get("start", 0))
    limit = int(request.args.get("limit", 10))
    sort = request.args.get("sort", "cnpj")
    direction = request.args.get("dir", "asc")

    companies_sorted = sorted(
        companies,
        key=lambda company: company[sort],
        reverse=direction.lower() == "desc",
    )
    companies_paginated = companies_sorted[start : start + limit]

    return jsonify(companies_paginated)
