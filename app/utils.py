def get_status_message(application):
    if application.status == "PENDING":
        return {
            "title": "Application Under Review",
            "message": "Your application is currently under review. You will be notified via SMS/Email once the status is updated. Please keep your documents ready for the next steps.",
            "type": "warning"
        }

    elif application.status == "APPROVED":
        return {
            "title": "Application Approved",
            "message": "Congratulations! Your application has been approved. Please check your email/SMS for next steps.",
            "type": "success"
        }

    elif application.status == "REJECTED":
        return {
            "title": "Application Rejected",
            "message": "Unfortunately, your application has not been approved. Contact school for more details.",
            "type": "danger"
        }

    else:
        return {
            "title": "Status Update",
            "message": "Your application status is not available right now.",
            "type": "info"
        }
    