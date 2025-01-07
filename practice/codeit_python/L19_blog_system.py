class Post:
    """게시글을 생성하고 관리하는 클래스"""
    
    def __init__(self, date: str, content: str):
        """게시글 초기화"""
        self.date = date
        self.content = content

    def __str__(self) -> str:
        """게시글 정보 문자열로 반환"""
        return "작성 날짜: {}\n내용: {}".format(self.date, self.content)

class BlogUser:
    """블로그 사용자와 게시글을 관리하는 클래스"""
    
    def __init__(self, name: str):
        """사용자 초기화 및 빈 게시글 리스트 생성"""
        self.name = name 
        self.posts = []  # 게시글 저장용 리스트

    def add_post(self, date: str, content: str):
        """새 게시글 추가"""
        new_post = Post(date, content)
        self.posts.append(new_post)

    def show_all_posts(self):
        """모든 게시글 출력"""
        for post in self.posts:
            print(post)

    def __str__(self) -> str:
        """사용자 정보 문자열로 반환"""
        return f"안녕하세요 {self.name}입니다.\n"


if __name__ == "__main__":
    # 테스트 코드
    blog_user_1 = BlogUser("성태호")
    print(blog_user_1)
    
    blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이었다.
많은 사람들이 축하해줬다.
행복했다.
""")
    blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")
    
    blog_user_1.show_all_posts()
