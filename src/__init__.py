try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-pagerduty').version
except Exception, e:
    VERSION = 'unknown'
