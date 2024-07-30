from flask import Flask, redirect, url_for
from flask_login import LoginManager, current_user, login_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于保持会话安全

login_manager = LoginManager()
login_manager.init_app(app)

# 假设有一个用户加载函数
@login_manager.user_loader
def load_user(user_id):
    # 根据 user_id 加载用户
    return User.get(user_id)

@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))  # 如果用户未认证，重定向到登录页面
    # 处理已认证用户的逻辑
    return 'Welcome, ' + current_user.username

@app.route('/login')
def login():
    # 这里应该有登录逻辑
    # 例如: login_user(user)
    return 'Login Page'

if __name__ == '__main__':
    app.run(debug=True,port=3000)
