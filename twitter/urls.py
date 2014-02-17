from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'twitts.views.index'),
     url(r'^followers$', 'twitts.views.followers'),
     url(r'^user_tweets$', 'twitts.views.display_user'),     
     url(r'^add_tweet$', 'twitts.views.add_tweet'),


    # url(r'^twitterro/', include('twitterro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
