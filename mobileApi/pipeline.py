from requests import request, HTTPError
from django.core.files.base import ContentFile
from mobileApi.models import Profile


def save_profile_picture(backend, user, response, details, is_new=False, *args, **kwargs):

    # Save Facebook profile photo into a user profile, assuming a profile model
    # with a profile_photo file-type attribute
    if backend.__class__.__name__ == 'FacebookOAuth2':

        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        profile = Profile.objects.get_or_create(user=user)
        profile[0].profile_picture = url
        profile[0].save()
