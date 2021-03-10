class Campaign(object):
    """An ad campaign we can serve to users."""

    def __init__(self, name, bid_price, target_keywords_list):
        """
        :param name: unique name for this campaign, e.g. "Nike Shoes Summer 2014"
        :param bid_price: amount to bid on any auctions when serving this campaign, e.g. 0.5
        :param target_keywords_list: list of keywords we are targeting for this campaign
        """
        self.name = name
        self.bid_price = bid_price
        self.target_keywords = set(target_keywords_list)

    def __str__(self):
        return "<Campaign - name={name}, bid_price={bid_price}, target_keywords={target_keywords}>".format(**self)


def choose_best_campaign_for_user(search_terms_list, campaigns):
    """Returns the best campaign to serve for a given user or None if
    no campaigns are applicable. A user can be served a campaign if they
    have searched for at least one keyword configured for the campaign.
    The "best" campaign to serve is the one with the most search term
    matches.
    If two or more campaigns have the same number of matches then the
    one with the highest bid_price should be served.
    If two or more campaigns have the same number of matches and the
    same bid_price then it should be a random pick between these campaigns.

    :param search_terms_list: list of search terms. assume normalized
    :param campaigns: a collection of Campaign objects
    :return: A single campaign object considered the 'best' campaign to show for the search terms provided
    """
    from random import random
    searches = set(search_terms_list)
    results = []
    for campaign in campaigns:
        match = len(searches & campaign.target_keywords)
        if match:
            results.append((match, campaign.bid_price, random(), campaign))
    if not results:
        return None
    results = sorted(results, key=lambda x: (x[0], x[1], x[2]))
    return results[0][3]
