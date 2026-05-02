import subprocess


def run(inputs: dict[str, str]) -> dict[str, str]:
    try:
        # executing the command as a list to avoid shell injection vulnerabilities
        subprocess.run(["sudo", "systemctl", "start", "hexbox-updater"], check=True)
        return {"message": "Refresh the page for updates to take effect."}

    except subprocess.CalledProcessError as e:
        # Handle cases where the command fails (e.g., service not found or permission denied)
        return {"message": f"Failed to start update: {str(e)}"}

    except Exception as e:
        return {"message": f"An unexpected error occurred: {str(e)}"}
