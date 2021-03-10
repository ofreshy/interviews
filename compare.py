st_235076 = {
    "id": 235076,
    "rtb_id": 235076,
    "created_at": "2017-04-18 17:20:58",
    "updated_at": "2017-04-20 15:48:35",
    "seller_lists_targeting_mode": None,
    "type": "Strategy",
    "parent_strategy_id": None,
    "temporary_id": None,
    "target_devices": "desktop_web",
    "target_browsers": "safari,chrome,opera,firefox,ie,other",
    "target_operating_systems": "windows,linux,android,osx,ios,other",
    "segment_targeting_mode": "ANY",
    "site_list_id": None,
    "site_list_role": None,
    "name": "TTD_Scotts_Ortho_OFAK_PreRoll (RON)",
    "bid_cpm": 5.23,
    "above_fold_cpm": None,
    "active": 1,
    "monthly_impression_cap": None,
    "daily_impression_cap": 40000,
    "one_user_impression_period": None,
    "monthly_budget": None,
    "daily_budget": None,
    "monthly_user_impressions": None,
    "daily_user_impressions": 4,
    "target_dayparts": "{\"Sunday\":[[0,23]],\"Monday\":[[0,23]],\"Tuesday\":[[0,23]],\"Wednesday\":[[0,23]],\"Thursday\":[[0,23]],\"Friday\":[[0,23]],\"Saturday\":[[0,23]]}",
    "line_item_id": 23870,
    "replicable": 1,
    "optimization_id": None,
    "deleted_at": None,
    "data_provider_targeting_role": None,
    "data_provider_targeting_type": None,
    "pacing_mode": "FLAT",
    "reportable_type": "RON",
    "viewability_threshold": None,
    "cross_device_enabled": 1,
    "ab_test_group_id": None,
    "external_segment_id": None,
    "intended_inventory": "any",
}

st_235565 = {
    "id": 235565,
    "rtb_id": 235565,
    "created_at": "2017-04-21 17:51:11",
    "updated_at": "2017-05-09 14:23:27",
    "seller_lists_targeting_mode": None,
    "type": "Strategy",
    "parent_strategy_id": None,
    "temporary_id": None,
    "target_devices": "desktop_web",
    "target_browsers": "safari,chrome,opera,firefox,ie,other",
    "target_operating_systems": "windows,linux,android,osx,ios,other",
    "segment_targeting_mode": None,
    "site_list_id": 1236,
    "site_list_role": "WHITE",
    "name": "John Deere Gator Discover OLV video - RON",
    "bid_cpm": 6.88,
    "above_fold_cpm": None,
    "active": 1,
    "monthly_impression_cap": None,
    "daily_impression_cap": None,
    "one_user_impression_period": None,
    "monthly_budget": None,
    "daily_budget": None,
    "monthly_user_impressions": None,
    "daily_user_impressions": 5,
    "target_dayparts": "{\"Sunday\":[[0,23]],\"Monday\":[[0,23]],\"Tuesday\":[[0,23]],\"Wednesday\":[[0,23]],\"Thursday\":[[0,23]],\"Friday\":[[0,23]],\"Saturday\":[[0,23]]}",
    "line_item_id": 24536,
    "replicable": 1,
    "optimization_id": None,
    "deleted_at": None,
    "data_provider_targeting_role": None,
    "data_provider_targeting_type": None,
    "pacing_mode": "FLAT",
    "reportable_type": "RON",
    "viewability_threshold": None,
    "cross_device_enabled": 1,
    "ab_test_group_id": None,
    "external_segment_id": None,
    "intended_inventory": "any",
}

for key, value in st_235076.items():
    if key in ("id", "rtb_id", "created_at", "updated_at", "name", "line_item_id"):
        continue
    other_value = st_235565[key]
    if other_value != value:
        diff = (key, value, other_value)
        print "key=%s, st_235076_value=%s, st_235565_value=%s" % diff