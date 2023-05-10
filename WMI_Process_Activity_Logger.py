{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'wmi'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-8b1c4889f7ee>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mwin32api\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mwin32security\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mwmi\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0msys\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'wmi'"
     ]
    }
   ],
   "source": [
    "import win32con\n",
    "import win32api\n",
    "import win32security\n",
    "import wmi\n",
    "import sys\n",
    "import os\n",
    "\n",
    "LOG_FILE = \"process_monitor_log.csv\"\n",
    "\n",
    "def get_process_privileges(pid):\n",
    "    try:\n",
    "        # Obtain a handle to the target process\n",
    "        hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION, False, pid)\n",
    "\n",
    "        # Open the main process token\n",
    "        htok = win32security.OpenProcessToken(hproc, win32con.TOKEN_QUERY)\n",
    "\n",
    "        # Retrieve the list of privileges enabled\n",
    "        privs = win32security.GetTokenInformation(htok, win32security.TokenPrivileges)\n",
    "\n",
    "        # Iterate over privileges and output the ones that are enabled\n",
    "        priv_list = []\n",
    "        for priv_id, priv_flags in privs:\n",
    "            # Check if the privilege is enabled\n",
    "            if priv_flags == 3:\n",
    "                priv_list.append(win32security.LookupPrivilegeName(None, priv_id))\n",
    "\n",
    "    except:\n",
    "        priv_list.append(\"N/A\")\n",
    "\n",
    "    return \"|\".join(priv_list)\n",
    "\n",
    "def log_to_file(message):\n",
    "    with open(LOG_FILE, \"a\") as fd:\n",
    "        fd.write(\"%s\\n\" % message)\n",
    "\n",
    "    return\n",
    "\n",
    "# Create a log file header\n",
    "if not os.path.isfile(LOG_FILE):\n",
    "    log_to_file(\"Time,User,Executable,CommandLine,PID,ParentPID,Privileges\")\n",
    "\n",
    "# Instantiate the WMI interface\n",
    "c = wmi.WMI()\n",
    "\n",
    "# Create our process monitor\n",
    "process_watcher = c.Win32_Process.watch_for(\"creation\")\n",
    "\n",
    "while True:\n",
    "    try:\n",
    "        new_process = process_watcher()\n",
    "\n",
    "        proc_owner = new_process.GetOwner()\n",
    "        proc_owner = \"%s\\\\%s\" % (proc_owner[0], proc_owner[2])\n",
    "        create_date = new_process.CreationDate\n",
    "        executable = new_process.ExecutablePath\n",
    "        cmdline = new_process.CommandLine\n",
    "        pid = new_process.ProcessId\n",
    "        parent_pid = new_process.ParentProcessId\n",
    "\n",
    "        privileges = get_process_privileges(pid)\n",
    "\n",
    "        process_log_message = \"%s,%s,%s,%s,%s,%s,%s\" % (create_date, proc_owner, executable, cmdline, pid, parent_pid, privileges)\n",
    "\n",
    "        print(process_log_message)\n",
    "\n",
    "        log_to_file(process_log_message)\n",
    "\n",
    "    except:\n",
    "        pass\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
