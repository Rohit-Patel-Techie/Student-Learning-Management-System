#Central Redirect Utility

def get_dashboard_url(user) : 
    if user.is_instructor() : 
        return 'instructor-dashboard'
    return 'student-dashboard'