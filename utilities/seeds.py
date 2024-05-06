from django.http import HttpResponse
from django.contrib.auth.models import User
from users.models import Teacher, Student
from extracurricular.models import Extracurricular, StudentExtracurricular, TeacherExtracurricular
from reports.models import Report
from olympiads.models import OlympiadField, OlympiadReport, OlympiadStudent
from grades.models import Grade
import csv
from django.utils import timezone


def seedDatabase(request):
    # with open('users.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined] in reader:
    #         user = User(
    #                 id = id,
    #                 username = username,
    #                 password = password,
    #                 email = email,
    #                 first_name = first_name,
    #                 last_name = last_name,
    #                 is_superuser = is_superuser,
    #                 is_staff = is_staff,
    #                 is_active = is_active,
    #                 date_joined = date_joined,
    #                 last_login = last_login if last_login != "NULL" else None,
    #             )
    #         user.save()

    # with open('teacher.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,nama_pembina,niy,jabatan,email,no_hp,foto,user_id,alamat,jenis_kelamin] in reader:
    #         user = Teacher(
    #             id = id,
    #             user_id = user_id,
    #             teacher_id = niy,
    #             teacher_code = None,
    #             teacher_name = nama_pembina,
    #             teacher_gender = jenis_kelamin,
    #             teacher_address = alamat,
    #             teacher_job = jabatan,
    #             teacher_email = email,
    #             teacher_phone = no_hp,
    #             teacher_photo = foto,
    #             is_active = 1,
    #             is_online = 0,
    #         )
    #         user.save()

    # with open('student.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,nama_siswa,nis,nisn,kelas,alamat,email,foto,jenis_kelamin,nomor_hp,status,tanggal_lahir,tempat_lahir] in reader:
    #         user = Student(
    #             id = id,
    #             student_nis = nis,
    #             student_nisn = nisn,
    #             student_nik = None,
    #             student_name = nama_siswa,
    #             student_class = kelas,
    #             student_gender = jenis_kelamin,
    #             student_address = alamat if alamat != "NULL" else None,
    #             student_birth_place = tempat_lahir if tempat_lahir != "NULL" else None,
    #             student_birth_date = tanggal_lahir if tanggal_lahir != "NULL" else None,
    #             student_email = email if email != "NULL" else None,
    #             student_phone = nomor_hp if nomor_hp != "NULL" else None,
    #             student_status = status if status != "NULL" else None,
    #             student_photo = foto if foto != "NULL" else None,
    #             student_batch = None,
    #         )
    #         user.save()

    # with open('ekskul.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,nama_ekskul,jadwal,waktu,tipe,slug,logo,deskripsi] in reader:
    #         ekskul = Extracurricular(
    #             id = id,
    #             extracurricular_name = nama_ekskul,
    #             extracurricular_schedule = jadwal,
    #             extracurricular_time = waktu,
    #             extracurricular_description = deskripsi,
    #             extracurricular_type = tipe,
    #             extracurricular_logo = logo,
    #             slug = slug,
    #         )
    #         ekskul.save()


    # with open('ekskulpembina.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,extracurricular_id,teacher_id] in reader:
    #         ekskul = TeacherExtracurricular(
    #             id = id,
    #             extracurricular_id = extracurricular_id,
    #             teacher_id = teacher_id,
    #         )
    #         ekskul.save()


    # with open('studentekskul.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,ekskul_id,siswa_id] in reader:
    #         ekskul = StudentExtracurricular(
    #             id = id,
    #             extracurricular_id = ekskul_id,
    #             student_id = siswa_id,
    #         )
    #         ekskul.save()


    # with open('report.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,tanggal_pembinaan,catatan_pembinaan,created_at,updated_at,nama_ekskul_id,pembina_ekskul_id,foto] in reader:
    #         report = Report(
    #             id = id,
    #             extracurricular_id = nama_ekskul_id,
    #             teacher_id = pembina_ekskul_id,
    #             report_date = tanggal_pembinaan,
    #             report_note = catatan_pembinaan,
    #             report_photo = foto,
    #         )
    #         report.save()

    # with open('report_student_presence.csv', 'r') as file_students:
    #     reader_students = csv.reader(file_students)
    #     for [id,report_id,studentorganization_id] in reader_students:
    #         try:
    #             report = Report.objects.get(pk=report_id)
    #             student = StudentExtracurricular.objects.get(pk=studentorganization_id)
    #             report.students.add(student)
    #             report.save()
    #         except:
    #             print("Error")


    # with open('osnfield.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,nama_bidang,jadwal_bimbingan,slug,pembimbing_id] in reader:
    #         osn = OlympiadField(
    #             id = id,
    #             olympiad_field_name = nama_bidang,
    #             olympiad_field_teacher_id = pembimbing_id,
    #             olympiad_field_schedule = jadwal_bimbingan,
    #             slug = slug,
    #         )
    #         osn.save()


    # with open('osnstudent.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,bidang_osn_id,nama_siswa_id] in reader:
    #         osn = OlympiadStudent(
    #             id = id,
    #             olympiad_field_id = bidang_osn_id,
    #             olympiad_student_id = nama_siswa_id,
    #         )
    #         osn.save()


    # with open('osnreport.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,tanggal_pembinaan,foto_bimbingan,materi_pembinaan,created_at,updated_at,bidang_osn_id,pembimbing_osn_id] in reader:
    #         osn = OlympiadReport(
    #             id = id,
    #             olympiad_field_id = bidang_osn_id,
    #             olympiad_level = "Kota/Kab",
    #             olympiad_practice_date = tanggal_pembinaan,
    #             photo = foto_bimbingan,
    #             notes = materi_pembinaan,
    #         )
    #         osn.save()

    # with open('osnreport_student_presence.csv', 'r') as file_students:
    #     reade_students = csv.reader(file_students)
    #     for [id,laporanosn_id,siswaosn_id] in reade_students:
    #         try:
    #             osn = OlympiadReport.objects.get(pk=laporanosn_id)
    #             student = OlympiadStudent.objects.get(pk=siswaosn_id)
    #             osn.students.add(student)
    #             osn.save()
    #         except:
    #             print("Error")

    # with open('grade.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for [id,nilai,created_at,updated_at,siswa_id] in reader:
    #         osn = Grade(
    #             id = id,
    #             student_id = siswa_id,
    #             grade = nilai,
    #             semester = "Ganjil",
    #         )
    #         osn.save()
    return HttpResponse("Seeding Database Done!")