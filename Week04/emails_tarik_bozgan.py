class Emails(list):
    def __init__(self, emails):
        # Tekrarlayan elemanları temizlemek için set kullanıyoruz
        # test_validate_duplicates testi bunu gerektiriyor.
        super().__init__(set(emails))
        self.validate()

    def validate(self):
        for email in self:
            # Sadece string veri tipine izin ver
            if not isinstance(email, str):
                raise ValueError("Only strings are allowed")
            
            # Basit e-posta format kontrolü: '@' ve sonrasında '.' olmalı
            if "@" not in email:
                raise ValueError("Invalid email: missing @")
            
            domain = email.split("@")[-1]
            if "." not in domain:
                raise ValueError("Invalid email: missing dot in domain")

    def __repr__(self):
        # Sınıfın string temsili: Emails(['a@b.com', ...]) formatında
        return f"Emails({super().__repr__()})"

    def __str__(self):
        return self.__repr__()