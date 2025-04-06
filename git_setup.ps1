# Initialize Git
git init

# Add remote origin
git remote add origin https://github.com/saikuma1r/COES.git

# Show remotes
git remote -v

# Stage all files
git add .

# Configure Git identity (global)
git config --global user.email "saikumap@gmail.com"
git config --global user.name "saikuma1r"

# Commit changes
git commit -m "Initial commit"

# Push to GitHub main branch
git push -u origin main
