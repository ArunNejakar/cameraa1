import os

class CameraApprovalManager:
    def _init_(self):
        self.requests = {}

    def request_camera(self, slot, hours, priority):
        self.requests[slot] = (hours, priority)

    def approval_status(self, slot):
        hours, priority = self.requests.get(slot, (0, 0))

        score = (hours * 10) - (priority * 5)

        if score <= 20:
            return "APPROVED"
        else:
            return "NOT APPROVED"


# -------- Jenkins Execution Entry --------
if __name__ == "__main__":

    camera = os.getenv("CAMERA_ID")
    slot = os.getenv("BOOKING_SLOT")
    hours = os.getenv("HOURS_REQUIRED")
    priority = os.getenv("PRIORITY_LEVEL")

    if not camera or not slot or not hours or not priority:
        print("ERROR: Jenkins parameters missing")
        exit(1)

    hours = int(hours)
    priority = int(priority)

    manager = CameraApprovalManager()
    manager.request_camera(slot, hours, priority)

    print("===== CAMERA BOOKING DECISION =====")
    print("Camera ID   :", camera)
    print("Slot        :", slot)
    print("Hours       :", hours)
    print("Priority    :", priority)
    print("Status      :", manager.approval_status(slot))
