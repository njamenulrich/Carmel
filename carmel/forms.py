from django.contrib.auth.forms import UserCreationForm
from users.models import Users

class UsersCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ("email", "name", "role")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # --- KEY STEP: Filter the choices for the 'role' field ---
        if 'role' in self.fields:
            # Get all choices defined in the model
            all_choices = self.fields['role'].choices
            
            # Filter out the 'Admin' choice
            # Filter choices where the first item (the value saved to the DB) is NOT 'Admin'
            filtered_choices = [
                choice for choice in all_choices 
                if choice[0] != 'Admin'
            ]
            
            # Assign the filtered list back to the form field
            self.fields['role'].choices = filtered_choices