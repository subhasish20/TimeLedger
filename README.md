# ⏱️ TimeLedger

A desktop screen-time tracking application for understanding how you spend time on your computer.

## 📖 Overview

TimeLedger is a desktop screen-time tracking application that monitors and records how much time the user spends on their computer. It is intended to help users understand their computer usage patterns.

🎯

The project addresses the lack of simple, local visibility into daily computer activity. By tracking active usage over time, TimeLedger can help users review where their time is going and make more informed decisions about their computer habits.

✨

## 🚀 Features

TimeLedger provides:

* 🖥️ Screen-time tracking for computer usage.
* 🔍 Active application or window detection using `kdotool`.
* ⏱️ Time accumulation based on the currently active task or window.
* 📊 Recording or displaying collected usage information.
* 🐍 Python-based application structure.
* ▶️ Shell script for starting the application.

⚠️

The exact feature set depends on the implementation in the current source code.

## 🔄 How It Works

The application monitors computer usage and records time spent on activities.

A typical workflow is:

1. **🔎 Detect the active application or window**

   TimeLedger uses `kdotool` to detect the currently active window or application.

2. **⏱️ Track usage time**

   While an application or task is active, TimeLedger tracks the amount of time spent on it.

3. **📊 Process usage information**

   The Python application processes the detected activity and maintains the required tracking information.

4. **💾 Record or display collected information**

   The collected usage information is handled by the application according to the current implementation.

5. **▶️ Start through `run.sh`**

   The `run.sh` script provides the main way to start TimeLedger and handles launching the Python application.

## 📁 Project Structure

```text
TimeLedger/
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
├── run.sh
└── TimeLedger
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-314.pyc
    │   └── TimeLedger.cpython-314.pyc
    └── TimeLedger.py
```

### 📄 File and Directory Description

* `main.py`

  The main Python entry point of the application. It starts the TimeLedger application.

* `run.sh`

  The shell script used to launch TimeLedger. It provides a convenient way to start the application without manually typing the Python command.

* `requirements.txt`

  Contains the Python packages required by TimeLedger.

* `TimeLedger/`

  Python package containing the main TimeLedger application code.

* `TimeLedger/TimeLedger.py`

  Contains the main TimeLedger application logic.


* `LICENSE`

  Contains the project's license information.

* `README.md`

  Documentation for the project.

## 🛠️ Requirements

### 🐍 Python

TimeLedger requires Python 3.

Check your installed Python version:

```bash
python --version
```

Or:

```bash
python3 --version
```

### 📚 Python Dependencies

Install the packages listed in `requirements.txt`.

### 🪟 `kdotool`

`kdotool` is required for active window/application detection.

## 🐧 Installing `kdotool` on Arch Linux / CachyOS

On Arch Linux or CachyOS:

```bash
sudo pacman -Sy kdotool
```

Make sure `kdotool` is available:

```bash
kdotool --version
```

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/subhasish20/TimeLedger.git
cd TimeLedger
```

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

If your system uses `python3`:

```bash
python3 -m pip install -r requirements.txt
```

Install `kdotool` on Arch Linux / CachyOS:

```bash
sudo pacman -Sy kdotool
```

## 🚀 Usage

### ▶️ Recommended Method — `run.sh`

The recommended way to start TimeLedger is through the provided `run.sh` script.

First, make the script executable:

```bash
chmod +x run.sh
```

Then run:

```bash
./run.sh
```

This starts the TimeLedger application using the project's configured run script.

### 🐍 Run Directly with Python

You can also start the application directly through `main.py`:

```bash
python main.py
```

Or:

```bash
python3 main.py
```

### 🔧 If `run.sh` Is Not Executable

You can run the script through Bash without changing its executable permission:

```bash
bash run.sh
```

## 🔄 Running TimeLedger

The recommended startup workflow is:

```text
run.sh
   │
   ▼
main.py
   │
   ▼
TimeLedger/TimeLedger.py
   │
   ▼
TimeLedger starts tracking
   │
   ▼
kdotool detects the active window/application
   │
   ▼
Usage information is processed
```

Therefore, users normally do **not** need to run `TimeLedger/TimeLedger.py` directly.

Use:

```bash
./run.sh
```

as the primary command.

## 🐧 Linux Compatibility

`kdotool` is required for TimeLedger's active-window detection.

The documented installation command uses Arch Linux/CachyOS package management:

```bash
sudo pacman -Sy kdotool
```

The current implementation is primarily oriented toward Linux systems where `kdotool` is available.

Support for other operating systems or desktop environments depends on whether the required window-detection functionality is available.

## 🔧 Configuration

No separate configuration file is currently included in the project structure.

Before running TimeLedger, make sure:

1. Python 3 is installed.
2. Python dependencies are installed.
3. `kdotool` is installed.
4. `kdotool` is available in your system `PATH`.
5. `run.sh` has executable permission.

You can verify the required commands with:

```bash
python --version
```

```bash
kdotool --version
```

## 🔮 Future Improvements

Possible future improvements include:

* 📊 Graphical dashboard.
* 📅 Daily, weekly, and monthly reports.
* 📈 Usage charts and visualizations.
* 🗂️ Application categories.
* ⚙️ Configurable tracking intervals.
* 🔔 Desktop notifications.
* 📤 Export to CSV or JSON.
* 🖥️ Support for additional desktop environments.
* 🚀 Automatic startup with the desktop session.

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

## 📜 License

See the `LICENSE` file for license information.

## 👤 Author / Contact

**Subhasish Jena**

GitHub: https://github.com/subhasish20

Email: [subhasishjena8280@gmail.com](mailto:subhasishjena8280@gmail.com)
