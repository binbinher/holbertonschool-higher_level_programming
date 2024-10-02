 #!/usr/bin/python3#!/usr/bin/python3
"""
A module that contains a class Student.
"""

class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.
        
        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.
      
        Args:
            attrs (list, optional): A list of attribute names to retrieve.
                                    If None, all attributes are retrieved.
        
        Returns:
            dict: A dictionary containing the Student instance's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: self.__dict__[attr]
                for attr in attrs if attr in self.__dict__
            }

    def reload_from_json(self, json_dict):
        """Replaces all attributes of the Student instance with those from a dictionary.
        
        Args:
            json_dict (dict): A dictionary where keys match attribute names and
                              values are the new values for those attributes.
        """
        for key, value in json_dict.items():
            setattr(self, key, value)
