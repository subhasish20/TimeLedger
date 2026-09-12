# ⏱️ TimeLedger

A desktop screen-time tracking application for understanding how you spend time on your computer.

## 📖 Overview

TimeLedger is a desktop screen-time tracking application that monitors and records how much time the user spends on their computer. It is intended to help users understand their computer usage patterns.

🎯

The project addresses the lack of simple, local visibility into daily computer activity. By tracking active usage over time, TimeLedger can help users review where their time is going and make more informed decisions about their computer habits.

✨

## 🚀 Features

Based on the current repository and project description, TimeLedger is expected to provide:

* 🖥️ Screen-time tracking for computer usage.
* 🔍 Active application or window detection, supported by the required `kdotool` dependency.
* ⏱️ Time accumulation based on the currently active task or window.
* 📋 Task-related handling through `tasklist.py`.
* 📊 Recording or displaying collected usage information.
* 🐍 A Python-based entry point and supporting shell script for running the tracking workflow.

⚠️

The exact feature set depends on the current source code. Features not visible from the repository structure are not claimed here.

⚙️

## 🔄 How It Works

The application monitors computer usage and records time spent on activities. A typical workflow is expected to be:

1. **🔎 Detect the active application or window**
   TimeLedger requires `kdotool`. This suggests that active window or application detection depends on `kdotool` being installed and available on the system.

2. **⏱️ Track usage time**
   While an application or task is active, TimeLedger records the time spent on it.

3. **📋 Process and maintain task information**
   `tasklist.py` likely contains logic related to handling tasks or tracked items. The exact implementation should be checked in the source file.

4. **💾 Record or display collected information**
   The application stores or presents the collected usage data in some form. The current repository structure does not document a graphical dashboard, so this should be treated as implementation-dependent.

✅

Confirmed behavior from the project description: TimeLedger monitors and records how much time the user spends on the computer. Confirmed dependency: `kdotool` is required for correct operation.

📁

## 🗂️ Project Structure

```text
TimeLedger/
├── main.py
├── tasklist.py
├── tracetime.sh
└── requirements.txt
```

* `main.py`
  Likely the main Python entry point for the application. It probably starts the tracking process and coordinates other components.

* `tasklist.py`
  Likely contains task-related logic, such as managing tracked tasks or organizing usage information.

* `tracetime.sh`
  A shell script likely used to start, manage, or support the time-tracking workflow. Inspect the script for exact usage.

* `requirements.txt`
  Lists the Python dependencies required by the project.

🛠️

## 📦 Requirements

* 🐍 Python
  A specific Python version is not documented in the repository structure. Use a currently supported Python 3 version.

* 📚 Python dependencies
  Install the packages listed in `requirements.txt`.

* 🪟 `kdotool`
  Required for the application to work correctly. `kdotool` is used for active window or application detection.

🐧

### 🐧 Installing `kdotool` on Arch Linux / CachyOS

```bash
sudo pacman -Sy kdotool
```

📥

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/subhasish20/TimeLedger.git
cd TimeLedger
```

📦

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

🐍

If your system uses `python3`, use:

```bash
python3 -m pip install -r requirements.txt
```

🔧

Install the required `kdotool` dependency on Arch Linux / CachyOS:

```bash
sudo pacman -Sy kdotool
```

▶️

## 🚀 Usage

The exact run command depends on the intended entry point in the current source code. The primary Python entry point appears to be `main.py`.

▶️

Run the application with:

```bash
python main.py
```

🐍

Or, if your system uses `python3`:

```bash
python3 main.py
```

🖥️

If the project is intended to be launched through the provided shell script, inspect `tracetime.sh` first and then run it according to its contents. For example:

```bash
bash tracetime.sh
```

⚠️

Because the repository listing alone does not confirm the exact startup workflow, use the appropriate Python entry point for your setup.

🐧

## 🐧 Linux Compatibility

`kdotool` is required for TimeLedger to work correctly. The installation command shown in this README targets Arch Linux and CachyOS package management.

🎯

For that reason, the current implementation is particularly oriented toward Linux systems using Arch/CachyOS package management. Support for other operating systems or desktop environments is not claimed unless verified in the source code.

⚙️

## 🔧 Configuration

No configuration files or configuration options are documented in the current repository structure.

📌

At minimum, ensure that `kdotool` is installed and available in your system `PATH`. If additional configuration is required, it should be documented after reviewing the source files.

🚀

## 🔮 Future Improvements

The following are possible future improvements, not existing features unless already implemented in the source code:

* 📊 Graphical dashboard.
* 📅 Daily, weekly, and monthly reports.
* 📈 Usage charts and visualizations.
* 🗂️ Application categories.
* ⚙️ Configurable tracking intervals.
* 🔔 Desktop notifications.
* 📤 Export to CSV or JSON.
* 🖥️ Support for additional desktop environments.

🤝

## 🤝 Contributing

Contributions are welcome.

1. 🍴 Fork the repository.
2. 🌿 Create a new branch for your change.
3. 🛠️ Make your changes.
4. ✅ Commit your changes with a clear message.
5. 📤 Push the branch to your fork.
6. 🔀 Open a pull request against the main repository.

📝

Please keep changes focused and describe what you modified in the pull request.

📜

## 📜 License

License information will be added here.

👤

## 👨‍💻 Author / Contact

**Subhasish Jena**
GitHub: https://github.com/subhasish20

Email: [subhasishjena8280@gmail.com](mailto:subhasishjena8280@gmail.com)

🔗

## 🌐 GitHub Repository

https://github.com/subhasish20/TimeLedger.git
