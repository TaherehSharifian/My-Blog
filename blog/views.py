from django.shortcuts import render

from datetime import date
# Create your views here.

post_list = [
    {
        'slug': 'django-programing',
        'image': 'django.png',
        'author': 'Tari',
        'date': date(2022,2,13),
        'title': 'Being a DJANGO Programmer',
        'summary': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cum, hic!',
        'content': '''
        Aliquam ac ligula et massa luctus convallis non ac purus. In sed pretium justo, eu pretium neque. Duis eu massa ultrices, euismod neque cursus, scelerisque dui. Curabitur pellentesque gravida tellus a bibendum. Etiam dignissim ullamcorper gravida. Quisque id scelerisque ligula, vel rhoncus eros. Curabitur a commodo velit, a suscipit ante. Nulla consectetur nulla libero, sit amet aliquam lectus cursus sed.
        ''',
    },
    {
        'slug': 'mountain-hiking',
        'image': 'hiking.png',
        'author': 'Tari',
        'date': date(2022,5,20),
        'title': 'Mountain hiking',
        'summary': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cum, hic!',
        'content': '''
        Proin tempus urna vulputate ligula dapibus porttitor. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed vitae placerat tortor, non tempor leo. Praesent id urna commodo, cursus quam eu, egestas massa. Vestibulum non massa orci. In eu dictum augue. Sed a interdum nisl, vitae condimentum ante. In porttitor libero ut sem finibus viverra.

Pellentesque finibus maximus arcu at vestibulum. Curabitur convallis imperdiet est ac dictum. Nunc consectetur rutrum rutrum. Morbi eleifend, massa eget tristique bibendum, augue nunc fringilla urna, lobortis porttitor est sem eu urna. Donec quis mi elementum, tristique elit in, gravida est. Quisque id tellus ut ex mollis rhoncus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
        ''',
    },
    {
        'slug': 'planning-the-day',
        'image': 'planing.jpg',
        'author': 'Tari',
        'date': date(2022,8,3),
        'title': 'Planing the day',
        'summary': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cum, hic!',
        'content': '''
        Phasellus vestibulum, lorem ac molestie aliquet, justo ipsum faucibus leo, at auctor risus erat dignissim ipsum. Quisque at ante pharetra, sodales mauris ac, laoreet libero. Cras pretium leo sit amet orci sollicitudin, eget sagittis urna faucibus. Fusce in placerat dui, vitae dictum lacus. Curabitur porttitor, quam vel ornare placerat, augue tortor ultrices urna, pulvinar egestas metus mi pulvinar quam. Ut dictum vitae lorem ut porta. Maecenas auctor nibh eu nisl hendrerit tristique. Nam commodo congue nibh eget facilisis. Fusce odio dolor, varius id mattis sit amet, tempus et nisi. Fusce ullamcorper, turpis id mattis fringilla, sem magna ornare nisi, id tristique felis sapien a tellus. Etiam eu dui dapibus nisi sagittis auctor vitae ac magna. Nunc vel neque a lectus pretium viverra lacinia ut odio. Fusce a auctor magna. Vivamus pulvinar sollicitudin erat vitae vehicula. Cras convallis et tortor eu imperdiet.
        ''',
    },
    {
        'slug': 'getting-the-c2-cefr',
        'image': 'CEFR_C2.jpeg',
        'author': 'Tari',
        'date': date(2022,7,5),
        'title': 'getting the C2 CEFR',
        'summary': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cum, hic!',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean suscipit nibh eros, ut molestie augue cursus et. Aliquam vestibulum rhoncus est eget hendrerit. Integer rhoncus turpis urna, porttitor faucibus sem imperdiet eu. Praesent id leo nec diam ornare molestie. In ut felis a libero sollicitudin lobortis efficitur sit amet ante. Nunc purus felis, eleifend eget ante id, pretium finibus purus. Proin ac felis sit amet felis elementum dignissim. Praesent quis tristique diam. Duis non dignissim nisl. Nullam suscipit et sapien a consequat. Sed pulvinar risus sit amet sem feugiat, at ultrices dui varius.

        Cras sed est ornare, congue leo vel, hendrerit diam. Cras consequat hendrerit odio, non fermentum neque facilisis a. Duis tincidunt dui nulla, ac feugiat neque lobortis ac. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed convallis semper neque et ullamcorper. Maecenas sit amet posuere risus, nec posuere magna. Vivamus quis euismod leo, sed ornare lectus. Mauris eget velit arcu. Sed tellus sem, porta facilisis placerat at, luctus eget eros. Mauris dapibus eros et finibus hendrerit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nec pellentesque arcu. Morbi augue urna, tincidunt vitae pretium nec, consequat eu urna.
        ''',
    },
]

def starting_page(request):
    context = {'posts': post_list[-3:]}
    return render(request, 'blog/index.html', context)

def posts(request):
    context = {'posts': post_list}
    return render(request, 'blog/all-posts.html', context)

def post_detail(request, slug):
    post = next(post for post in post_list if post['slug']==slug)
    context = {'post':post}
    return render(request, 'blog/post-detail.html', context)