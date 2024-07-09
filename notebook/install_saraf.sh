#!/bin/bash

# Function to check if a Python library is installed
check_and_install() {
    package=$1
    import_name=$2
    if python3 -c "import $import_name" &> /dev/null; then
        echo "Library '$package' ($import_name) is already installed."
    else
        echo "Library '$package' ($import_name) is not installed. Installing now..."
        pip install $package
        if [ $? -eq 0 ]; then
            echo "Library '$package' installed successfully."
        else
            echo "Failed to install library '$package'. Please install it manually."
            exit 1
        fi
    fi
}

# Step 1: Download saraf.py using wget
echo "Downloading saraf.py from GitHub..."
wget https://raw.githubusercontent.com/moshtaqtsr/SARAF/main/notebook/saraf.py -O saraf.py
if [ $? -ne 0 ]; then
    echo "Failed to download saraf.py. Please check the URL and try again."
    exit 1
fi

# Step 2: Make saraf.py executable and move it to a directory in your PATH
chmod +x saraf.py
sudo mv saraf.py /usr/local/bin/saraf

# Step 3: Check and Install Required Libraries
required_libraries=(
    "biopython:Bio"
)

echo "Checking and installing required Python libraries..."
for lib in "${required_libraries[@]}"; do
    package=${lib%%:*}
    import_name=${lib##*:}
    check_and_install $package $import_name
done

echo "Installation complete. You can now run 'saraf' from any directory."
echo "All required libraries are installed."
