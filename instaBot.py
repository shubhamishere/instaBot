import requests                     #importing the requests library that is installed using pip.

ACCESS_TOKEN = '2040602664.73d62c1.c809539a12604d7191c64d239b67baef'
BASE_URL = 'https://api.instagram.com/v1/'
payload = {'access_token':ACCESS_TOKEN}



def self_info():                        #function to print my instagram profile details.
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
    my_info = requests.get(request_url).json()
    print 'My Info is: \n'
    print 'Short Bio: ' + my_info['data']['bio']
    print 'My Website: ' + my_info['data']['website']
    print 'My Username: ' + my_info['data']['username']
    print 'I follow ' + str(my_info['data']['counts']['follows']) + ' Users'
    print 'I am followed by: ' + str(my_info['data']['counts']['followed_by']) + ' Users!'
    print 'No. of media uploaded by me are: ' + str(my_info['data']['counts']['media'])

#self_info()

def get_user_id_by_username(insta_username):            #this function will return the userID of the entered instagram username
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

#get_user_id_by_username('rajat8310')

def get_user_recent_posts(insta_username):              #This function will simply get some of the recent uploaded posts by the user.

    user_id = get_user_id_by_username(insta_username)
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'Requesting URL for Data: ' + request_url

    recent_post = requests.get(request_url).json()
    #print recent_post
    if recent_post['meta']['code'] == 200:
        if len(recent_post['data']):
            return recent_post['data'][0]['id']
        else:
             print 'No recent post by this user!'
    else:
        print 'Status code other than 200'

print get_user_recent_posts('rajat8310')


def like_a_userPost(insta_username):                        #Function to like the user post, it will like the post id that we fetched in the above funtion.
    post_id = get_user_recent_posts(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (post_id)
    like_a_userPost = requests.post(request_url,payload).json()
    if like_a_userPost['meta']['code']==200:
        print "Like was successful"
    else:
        print "Like not successful"

#like_a_userPost('rajat8310')

def comment_on_a_userPost(insta_username):                  #To comment on the post whose post id fetched in the above function.
    post_id = get_user_recent_posts(insta_username)
    request_url = (BASE_URL + 'media/%s/comments') % (post_id)
    request_data = {'access_token':ACCESS_TOKEN, 'text':'this is instaBot commenting'}
    comment_on_a_post = requests.post(request_url, request_data).json()
    if comment_on_a_post['meta']['code'] == 200:
        print "Comment was successful"
    else:
        print "Comment Unsuccessful, please try again."

#comment_on_a_userPost('rajat8310')

def get_the_commentID(insta_username):                  #Search the comment by word and return its commentID.
    post_id = get_user_recent_posts(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (post_id, ACCESS_TOKEN)
    get_a_commentID = requests.get(request_url).json()
    wordInTheComment = raw_input("Enter a word that you think is in the comment:")
    if get_a_commentID['meta']['code']==200:
        for i in len(get_a_commentID['data']):
            if wordInTheComment in get_a_commentID['data'][i]['text']:
                print "Comment found"
                return get_a_commentID['data'][i]['id']
        else:
            print "No comment was found"
    else:
        print "Status code other than 200 was received"

#get_the_commentID('rajat8310')

def delete_comment_by_word(insta_username):                 #Delete the comment whose id we fetched above.
    post_id  = get_user_recent_posts(insta_username)
    comment_id = get_the_commentID(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/%s?access_token=%s') % (post_id, comment_id, ACCESS_TOKEN)
    deleting_comment = requests.delete(request_url).json()
    if deleting_comment['meta']['code']==200:
        print "This comment is deleted successfully"
    else:
        print "The comment was not successfully deleted"

#delete_comment_by_word('rajat8310')

condition = 'i'
instagramUsername = raw_input("Enter the instagram username for which you want perform actions: ")
if (condition=='i' or condition=='I'):
    print "The options of the actions that this bot can perform for you are given below:- \n\
    1. View details of your instagram profile. \n\
    2. Get profile ID of an instagram user. \n\
    3. Get user's recently uploaded posts. \n\
    4. Like the user's posts. \n\
    5. Comment on a user's post. \n\
    6. Search for a word in your comments of the post and get the comment ID. \n\
    7. Delete the searched comment (if any). \n "

    chooseOption = int(raw_input("Enter your option: "))
    if chooseOption==1:
        self_info()
    elif chooseOption==2:
        get_user_id_by_username(instagramUsername)
    elif chooseOption==3:
        get_user_recent_posts(instagramUsername)
    elif chooseOption==4:
        like_a_userPost(instagramUsername)
    elif chooseOption==5:
        comment_on_a_userPost(instagramUsername)
    elif chooseOption==6:
        get_the_commentID(instagramUsername)
    elif chooseOption==7:
        delete_comment_by_word(instagramUsername)
    else:
        print "Invalid selection!"

    condition = raw_input("Do you want to continue i/x: ")