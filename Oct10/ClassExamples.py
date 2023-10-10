class Student():
    """
    A class defining a university student
    """

    ID_Number = 0

    def __init__(self, name:str, age:int, major:str):
        """
        Constructor for a student instance
        
        Parameters
        ----------
        name : str
            The name of the student.
        age : int
            The age of the student.
        major : str
            The major of the student.

        """
        
        self.name = name
        self.age = age
        self.major = major

        self.ID = Student.ID_Number
        Student.ID_Number += 1

    def get_name(self):
        """
        Returns the name of the student.
        """

        return self.name


    def __repr__(self):
        """
        Returns a string representation of the student.
        """

        return f"Student('{self.name}', {self.age}, '{self.major}', ID: {self.ID})"
    

    def __le__(self, other):
        """
        Returns True if the student is younger than or the same age as another student.
        """

        return self.age <= other.age
    


class SSE_student(Student):


    def __init__(self, name:str, age:int, major:str):
        """
        Constructor for a student instance
        
        Parameters
        ----------
        name : str
            The name of the student.
        age : int
            The age of the student.
        major : str
            The major of the student.

        """
        super().__init__(name, age, major)

        self.ID = self.ID + 1000   # This is a bad idea, but it works

        
        super().__init__(name, age, major)

    def __repr__(self):
        """
        Returns a string representation of the student.
        """

        return "Schulich Student: " + super().__repr__()