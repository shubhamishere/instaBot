import requests
ACCESS_TOKEN = '2040602664.73d62c1.c809539a12604d7191c64d239b67baef'
BASE_URL = 'https://api.instagram.com/v1/'



def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
    my_info = requests.get(request_url).json()
    print 'My Info is: \n'
    print 'Short Bio: ' + my_info['data']['bio']
    print 'My Website: ' + my_info['data']['website']
    print 'My Username: ' + my_info['data']['username']
    print 'I follow ' + str(my_info['data']['counts']['follows']) + ' Users'
    print 'I am followed by: ' + str(my_info['data']['counts']['followed_by']) + ' Users!'
    print 'No. of media uploaded by me are: ' + str(my_info['data']['counts']['media'])

self_info()

def get_user_id_by_username(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, ACCESS_TOKEN)
    print 'Requesting URL for DATA: ' + request_url
    print
    search_results = requests.get(request_url).json()
    print search_results

    if search_results ['meta']['code'] == 200:
        if len(search_results['data']) > 0:
            print 'User ID: ' + search_results['data'][0]['id']
            return search_results['data'][0]['id']
        else:
            print 'No user found !'
    else:
        print 'Status code other than 200 was received'
    return None

get_user_id_by_username('sumit.pandey5895')

def get_user_recent_posts(insta_username):

    user_id = get_user_id_by_username(insta_username)
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'Requesting URL for Data: ' + request_url

    recent_post = requests.get(request_url).json()
    #print recent_post
    if recent_post['meta']['code'] == 200:
        if len(recent_post['data']):
            for recent in recent_post['data']:
                print recent['images']['standard_resolution']['url']
        else:
             print 'No recent post by this user!'
    else:
        print 'Status code other than 200'

print get_user_recent_posts('sumit.pandey5895')


