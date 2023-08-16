The fifth section assignment answer.

1.💡We can understand the cache as a temporary memory. We can store data in the caches just like in the database. But caches have advantages. In the cache, we can use the data that will be used several times without reserving space in the database.

🚫 But the cache has a useful side and a bad side, as I said earlier, the information in the cache is temporary and it will be deleted after some time.

2.Tests are very important for all programmers. Because when we are creating a program, diffirent problems may occur. So that these problems do not occur, we need to write automated tests. Python also has several Testing packages. For example, PyTest, UnitTest and others.

When creating a website in Django, we also need to write tests. This also ensures that our product is reliable.
For this we use TestCase.
For example:
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testUser',
            email='test@gmail.com',
            password='secret'
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title="A good title",
            body="Nice body content",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'testUser')
        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(self.post.body, 'Nice body content')
        self.assertEqual(str(self.post), 'A good title')
In this example, we first create User and Post models and check that the objects we created are created correctly.

3.First of all we need to know what Django ORM reletions are.
There are 3 types of relationships in Django.
These are:
✅ OneToOne,
✅ OneToMany,
✅ ManyToMany.

Through these methods, we can connect the models in different ways.

🚫 One of the most important and difficult tasks in programming is to run the program quickly. For example, we have a main page, and on this page, 3 queries go to the database. If 1 query takes 1 second, for 1000 users, we need 3000 seconds.

⚡️ To solve this problem, select_related and prefetch_related help us.
Select_related helps us collect OneToMany(ForeignKey) and OneToOne queries and send 1 query to the database.
Select_related helps to collect ManyToMany requests and send 1 request to the database.

🥳 Through these methods, our program works faster than before.

