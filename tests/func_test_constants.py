#encoding: utf-8

FORUMS = [
            { 
                'name': 'Forum With Sufficiently Large Name',
                'short_name': 'forumwithsufficientlylargename'
            },
            { 
                'name': 'Forum I',
                'short_name': 'forum1'
            },
            { 
                'name': 'Forum II',
                'short_name': 'forum2'
            },
            { 
                'name': u'Форум Три',
                'short_name': 'forum3'
            },
]


THREADS = [
            { 
                'title': 'Thread With Sufficiently Large Title',
                'slug': 'Threadwithsufficientlylargetitle',
                'date': '2014-01-01 00:00:01',
                'message': 'hey hey hey hey!',
                'isClosed': True,
                'isDeleted': True,

            },
            { 
                'title': 'Thread I',
                'slug': 'thread1',
                'date': '2013-12-31 00:01:01',
                'message': 'hey!',
                'isDeleted': False,
                'isClosed': False,
            },
            { 
                'title': 'Thread II',
                'slug': 'thread2',
                'date': '2013-12-30 00:01:01',
                'message': 'hey hey!',
                'isDeleted': False,
                'isClosed': False,
            },
            { 
                'title': u'Тред Три',
                'slug': 'thread3',
                'date': '2013-12-29 00:01:01',
                'message': 'hey hey hey!',
                'isDeleted': False,
                'isClosed': False,
            },
]

POSTS = [
            { 
                'message': 'my message 1',
                'isApproved': True,
                'isSpam': False,
                'isDeleted': False,
                'isEdited': True,
                'isHighlighted': True,
                'date': '2014-01-01 00:00:01',
                'childs':   [
                                { 
                                    'message': 'my message 3',
                                    'isApproved': False,
                                    'isSpam': False,
                                    'isDeleted': False,
                                    'isEdited': True,
                                    'isHighlighted': False,
                                    'date': '2014-01-01 00:02:01',
                                    'childs':   [
                                                    { 
                                                        'message': 'my message 1',
                                                        'isApproved': False,
                                                        'isSpam': True,
                                                        'isDeleted': False,
                                                        'isEdited': True,
                                                        'isHighlighted': False,
                                                        'date': '2014-01-02 00:02:01'
                                                    },
                                                ]
                                }
                            ]
            },
            { 
                'message': 'my message 1',
                'isApproved': True,
                'isSpam': False,
                'isDeleted': False,
                'isEdited': False,
                'isHighlighted': False,
                'date': '2014-01-03 00:01:01'
            },

            { 
                'message': 'my message 1',
                'isApproved': False,
                'isSpam': False,
                'isDeleted': True,
                'isEdited': False,
                'isHighlighted': False,
                'date': '2014-01-03 00:08:01'
            },
]


USERS = [
            {
                "username": "user1",
                "about":"hello im user1",
                "name":"John",
                "isAnonymous": False,
                "email":"example@mail.ru"
            },
            {
                "name": None,
                "isAnonymous": True,
                "email":"richard.nixon@example.com"
            },
            {
                "username": "user2",
                "about":"hello im user2",
                "name":"Jey",
                "isAnonymous": False,
                "email":"example2@mail.ru"
            },
            {
                "username": "user3",
                "about":"hello im user3",
                "name":"Josh",
                "isAnonymous": False,
                "email":"example3@mail.ru"
            },
            {
                "username": "user4",
                "about":"hello im user4",
                "name":"Jim",
                "isAnonymous": False,
                "email":"example4@mail.ru"
            },

]

TEST_CONF = {
    'forums': FORUMS,
    'threads': THREADS,
    'posts': POSTS,
    'users': USERS
}

TEST_FORUMS = {
    'listPosts': [
        {
            'forum': 'forumwithsufficientlylargename',
            'since': '2014-01-02 00:00:00',
            'limit': 2,
            'order': 'asc',
            'related': ['thread', ]
        },
        {
            'forum': 'forum1',
            'since': '2014-01-01 00:00:00',
            'order': 'desc',
            'related': ['thread', 'forum']
        },
        {
            'forum': 'forum2',
            'since': '2014-01-01 00:00:00',
            'order': 'desc',
        },
        {
            'forum': 'forum3',
            'since': '2014-01-03 00:00:00',
            'order': 'desc',
            'limit': 3,
        },
    ],
    'listThreads': [
        {
            'forum': 'forumwithsufficientlylargename',
            'since': '2013-12-30 00:00:00',
            'limit': 2,
            'order': 'asc',
            'related': ['forum', 'user']
        },
        {
            'forum': 'forum1',
            'since': '2013-12-31 00:00:00',
            'order': 'desc',
            'related': ['forum']
        },
        {
            'forum': 'forum2',
            'since': '2014-01-01 00:00:00',
            'order': 'desc',
            'related': ['user', ]
        },
        {
            'forum': 'forum3',
            'since': '2013-12-29 00:00:00',
            'order': 'desc',
            'limit': 3,
        },
    ],
    'listUsers': [
        {
            'forum': 'forumwithsufficientlylargename',
            'since_id': 10,
            'limit': 2,
            'order': 'asc',
        },
        {
            'forum': 'forum1',
            'order': 'desc',
        },
    ]
}

TEST_POSTS = {
    'list': [
        {
            'forum': 'forumwithsufficientlylargename',
            'since': '2014-01-02 00:00:00',
            'limit': 2,
            'order': 'asc',
        },
        {
            'forum': 'forum1',
            'since': '2014-01-01 00:00:00',
            'order': 'desc',
        },
        {
            'thread': 'thread2',
            'since': '2014-01-01 00:00:00',
            'order': 'desc',
        },
        {
            'thread': 'thread3',
            'since': '2014-01-03 00:00:00',
            'order': 'desc',
            'limit': 3,
        },
    ],
    'votes': 1,
}

TEST_THREADS = {
    'list': [
        {
            'forum': 'forumwithsufficientlylargename',
            'since': '2014-01-02 00:00:00',
            'limit': 2,
            'order': 'asc',
        },
        {
            'forum': 'forum1',
            'since': '2014-01-01 00:00:00',
            'order': 'desc',
        },
        {
            "user":"example2@mail.ru",
            'since': '2014-01-01 00:00:00',
            'order': 'desc',
        },
        {
            "user":"example3@mail.ru",
            'since': '2014-01-03 00:00:00',
            'order': 'desc',
            'limit': 3,
        },
    ],
    'votes': 1,
    'subscriptions': len(USERS),
    'unsubscriptions': 1,

}