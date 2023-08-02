from marshmallow import Schema, ValidationError, fields, validates


class CompanySchema(Schema):
    cnpj = fields.String(
        required=True,
        metadata={"description": "CNPJ"},
        validate=lambda s: len(s) == 14 and s.isdigit(),
        error_messages={
            "required": "CNPJ obrigatorio.",
            "validator_failed": "CNPJ deve conter exatamente 14 digitos.",
        },
    )
    company_name = fields.String(
        required=True,
        metadata={"description": "Razão Social"},
        error_messages={"required": "Razao Social -> obrigatorio."},
    )
    trading_name = fields.String(
        required=True,
        metadata={"description": "Nome Fantasia"},
        error_messages={"required": "Nome Fantasia -> obrigatorio."},
    )
    cnae = fields.String(
        required=True,
        metadata={"description": "CNAE"},
        error_messages={"required": "CNAE e obrigatorio."},
    )

    @validates("cnae")
    def validate_cnae(self, value):
        if not value.isdigit():
            raise ValidationError("CNAE deve ser um numero.")
        if len(value) not in (4, 6):
            raise ValidationError("CNAE deve conter 4 ou 6 digitos.")
