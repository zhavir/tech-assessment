class PasswordGeneratorService:
    def generate_password(
        self,
        *,
        password_length: int,
        has_numbers: bool,
        has_lowercase_chars: bool,
        has_uppercase_chars: bool,
        has_special_chars: bool,
    ) -> str:
        return "something"
