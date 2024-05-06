from django.utils.translation import gettext as _

extracurricular_types = (
        ("Ekskul", _("Extracurricular")),
        ("SC", _("Study Club"))
    )

extracurricular_times = (
        ("Pagi", _("Morning")),
        ("Siang", _("Evening")),
        ("Sore", _("Afternoon")),
        ("Malam", _("Night")),
    )

gender = (
    ("L", _("Male")),
    ("P", _("Female"))
)

# hari = (
#         ('Senin', _('Senin')),
#         ('Selasa', _('Selasa')),
#         ('Rabu', _('Rabu')),
#         ('Kamis', _('Kamis')),
#         ('Jumat', 'Jumat'),
#         ('Sabtu', 'Sabtu'),
#         ('Ahad', 'Ahad')
#     )


class_list = (
        ('X-MIPA-A', 'X-A'),
        ('X-MIPA-B', 'X-B'),
        ('X-MIPA-C', 'X-C'),
        ('X-MIPA-D', 'X-D'),
        ('X-MIPA-E', 'X-E'),
        ('X-MIPA-F', 'X-F'),
        ('X-MIPA-G', 'X-G'),
        ('X-MIPA-H', 'X-H'),
        ('XI-MIPA-A', 'XI-A'),
        ('XI-MIPA-B', 'XI-B'),
        ('XI-MIPA-C', 'XI-C'),
        ('XI-MIPA-D', 'XI-D'),
        ('XI-MIPA-E', 'XI-E'),
        ('XI-MIPA-F', 'XI-F'),
        ('XI-MIPA-G', 'XI-G'),
        ('XI-MIPA-H', 'XI-H'),
        ('XII-MIPA-A', 'XII-A'),
        ('XII-MIPA-B', 'XII-B'),
        ('XII-MIPA-C', 'XII-C'),
        ('XII-MIPA-D', 'XII-D'),
        ('XII-MIPA-E', 'XII-E'),
        ('XII-MIPA-F', 'XII-F'),
        ('XII-MIPA-G', 'XII-G'),
        ('XII-MIPA-H', 'XII-H'),
    )

semester_choice = (
    (None, _("Choose Semester")),
    ("Ganjil", _("Odd")),
    ("Genap", _("Even")),
)

olympiad_level = (
    (None, _("Choose Olympiad Level")),
    ("Sekolah", _("School")),
    ("Kota/Kab", _("City/Regency")),
    ("Provinsi", _("Province")),
    ("Nasional", _("Nasional")),
)

grade_choice = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
)