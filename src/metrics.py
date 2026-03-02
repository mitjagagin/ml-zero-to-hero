def calculate_accuracy(y_true, y_pred):
    correct = 0
    total = len(y_true)

    for i in range(total):
        if y_true[i] == y_pred[i]:
            correct += 1

    return correct / total

def calculate_precision(y_true, y_pred):
    tp = 0
    fp = 0

    for i in range(len(y_true)):
        true = y_true[i]
        pred = y_pred[i]

        if pred == 1:
            if true == 1:
                tp += 1
            else:
                fp += 1
    
    if (tp + fp)  == 0:
        return 0.0
    else:
        return tp / (tp + fp)
    
def get_model_report(y_true,  y_pred, model_name="MyModel"):
    acc = calculate_accuracy(y_true, y_pred)
    prec = calculate_precision(y_true, y_pred)

    return {
        "model": model_name,"accuracy": acc,
        "precision": prec
    }