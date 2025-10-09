Got it 👍 You’re running into this error because **your subproject’s virtual environment doesn’t have `pip` installed** (so PyCharm can’t install `notebook` or any other package into it).

Let’s go step by step:

---

### 🔍 Why the error happens

* PyCharm tries to run:

  ```
  .venv\Scripts\python.exe ... packaging_tool.py install notebook
  ```
* But inside that `.venv`, the `pip` module is **missing**.
* Normally, when you create a venv, `pip` should be installed automatically, but in Python 3.13 (still very new) some builds don’t include it.

---

### ✅ Fix

1. **Activate your subproject’s venv manually**

   ```powershell
   cd C:\Users\LifeD\PycharmProjects\example-agent\A09_Email_Refiner_Agent
   .venv\Scripts\activate
   ```

2. **Install pip into the venv**

   ```powershell
   python -m ensurepip --upgrade
   python -m pip install --upgrade pip setuptools wheel
   ```

   > If `ensurepip` is not available, install `pip` manually:

   ```powershell
   curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python get-pip.py
   ```

3. **Now install your notebook + dependencies**

   ```powershell
   pip install -r pyproject.toml
   ```

   or simply:

   ```powershell
   pip install notebook ipykernel
   ```

4. **Tell PyCharm to use this venv**

   * Go to **Settings → Project → Python Interpreter**
   * Select `.../A09_Email_Refiner_Agent/.venv/Scripts/python.exe`
   * Apply & restart PyCharm.

---

### ⚡ Additional Tips

* Since you’re working in **subprojects with their own `pyproject.toml`**, it’s better to use **uv** or **pip-tools** to sync dependencies cleanly:

  ```bash
  uv pip install -r pyproject.toml
  ```
* For running Jupyter notebooks in PyCharm:

  * Make sure `ipykernel` is installed in your subproject venv.
  * Restart the IDE → "Run Jupyter Notebook" should now detect the kernel.

---

👉 Question: Do you want me to show you how to set up **subproject isolation** (so PyCharm doesn’t try to mix main + sub dependencies), or just fix pip and run `notebook` inside the subproject venv?
