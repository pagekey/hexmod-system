import subprocess
from hex import Params


def run(params: Params) -> dict[str, str]:
    try:
        # Schedule the systemctl command to run in a transient timer 1 second from now
        subprocess.run(
            [
                "sudo",
                "systemd-run",
                "--on-active=1s",
                "systemctl",
                "start",
                "hexbox-updater",
            ],
            check=True,
        )

        return {"message": "Success! Refresh in 30 seconds."}

    except subprocess.CalledProcessError as e:
        return {"message": f"Failed to schedule update: {str(e)}"}
    except Exception as e:
        return {"message": f"An unexpected error occurred: {str(e)}"}
