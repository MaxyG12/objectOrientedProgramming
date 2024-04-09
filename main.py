class job:
  name = None
  salary = None
  hours = None
  
  def __init__(self, name, salary, hours):
    self.name = name
    self.salary = salary
    self.hours = hours

  def print_job(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")

class doctor(job):
  speciality = None
  years_of_experience = None

  def __init__(self, speciality, years_of_experience):
    self.name = "Doctor"
    self.salary = "£50,000"
    self.hours = "50"
    self.speciality = speciality
    self.years_of_experience = years_of_experience

  def print_job(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")
    print(f"Speciality: {self.speciality}")
    print(f"Years of experience: {self.years_of_experience}")

class teacher(job):
  subject = None
  position = None

  def __init__(self, subject, position):
    self.name = "Teacher"
    self.salary = "£35,000"
    self.hours = "40"
    self.subject = subject
    self.position = position

  def print_job(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")
    print(f"Subject: {self.subject}")
    print(f"Position: {self.position}")

lawyer = job("Lawyer", "£50,000", "60")
lawyer.print_job()

print()

teacher = teacher("Computer Science", "Classroom Teacher")
teacher.print_job()

print()

doctor = doctor("Paediatric Consultant", "7")
doctor.print_job()
