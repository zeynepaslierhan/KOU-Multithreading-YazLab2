import similarity_on_data as sm


def threading(column,threshold,threadsNumber):
    
    if column == "Product":
        column2=2
    if column == "Issue":
        column2=3

    sm.sm_onData(column2,threshold)