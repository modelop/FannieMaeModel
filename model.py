#modelop.score
def perform_prediction(data):
    yield data


#modelop.metrics
def perform_metrics(data):
    yield {'datasize': data.size}
