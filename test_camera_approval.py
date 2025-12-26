from camera_approval import CameraApprovalManager

def test_request_added():
    c = CameraApprovalManager()
    c.request_camera("9AM-11AM", 2, 3)
    assert c.requests["9AM-11AM"] == (2, 3)

def test_approved_booking():
    c = CameraApprovalManager()
    c.request_camera("9AM-11AM", 1, 4)
    assert c.approval_status("9AM-11AM") == "APPROVED"

def test_not_approved_booking():
    c = CameraApprovalManager()
    c.request_camera("3PM-7PM", 6, 1)
    assert c.approval_status("3PM-7PM") == "NOT APPROVED"
