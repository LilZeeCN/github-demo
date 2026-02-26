"""用户资料管理模块"""

class UserProfile:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.bio = ""
    
    def set_bio(self, bio):
        """设置个人简介"""
        self.bio = bio
        return True
    
    def get_profile(self):
        """获取用户资料"""
        return {
            "username": self.username,
            "email": self.email,
            "bio": self.bio
        }
    
    def update_email(self, new_email):
        """更新邮箱"""
        if "@" in new_email:
            self.email = new_email
            return True
        return False

if __name__ == "__main__":
    # 测试代码
    user = UserProfile("testuser", "test@example.com")
    user.set_bio("这是我的个人简介")
    print(user.get_profile())
