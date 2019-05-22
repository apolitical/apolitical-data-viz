def get_ts_tick_labels(df):

    """
    get_tick_labels

    Function for producing cleanly-formatted tick labels for DataFrames
    with a time-series index

    INPUTS:
        df - DataFrame with datetime Index from which to extract
             tick labels for plotting

    OUTPUTS:
        tick_labs - array of tick labels (one per day, minimally complex)

    """

    tick_labs = df.index.strftime("%d").values

    is_first_week_of_month = df.index.day <= 7
    is_first_week_of_year = df.index.dayofyear <= 7

    tick_labs[is_first_week_of_month] = df.index[is_first_week_of_month].strftime(
        "%d\n%b"
    )

    tick_labs[is_first_week_of_year] = df.index[is_first_week_of_year].strftime(
        "%d\n%b\n%Y"
    )

    return tick_labs


def get_ts_tick_labels_monthly(df):

    """
    get_ts_tick_labels_monthly

    Function for producing cleanly-formatted tick labels for DataFrames
    with a time-series index, one per week

    INPUTS:
        df - DataFrame with datetime Index from which to extract
             tick labels for plotting

    OUTPUTS:
        tick_labs - array of tick labels (one per month, minimally complex)

    """

    tick_labs = df.index.strftime("").values

    is_first_week_of_month = df.index.day <= 7
    is_first_week_of_year = df.index.dayofyear <= 7

    tick_labs[is_first_week_of_month] = df.index[is_first_week_of_month].strftime("%b")

    tick_labs[is_first_week_of_year] = df.index[is_first_week_of_year].strftime(
        "%b\n%Y"
    )

    return tick_labs
