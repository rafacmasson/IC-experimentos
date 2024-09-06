# CIC-IDS-2017

## Multiclass

### Cross-Validation Results of CIC-IDS-2017

| **Classifier** | **Score1** | **Score2** | **Score3** | **Score4** | **Score5** | **Mean** | **Standard Deviation** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.8893 | 0.8819 | 0.8862 | 0.8862 | 0.8161 | 0.8719 | 0.028 |
| K-Nearest Neighbors | 0.9978 | 0.9978 | 0.9977 | 0.9978 | 0.9978 | 0.9978 | 0 |
| Linear Discriminant Analysis | 0.9059 | 0.9057 | 0.9053 | 0.9061 | 0.9054 | 0.9057 | 0.0003 |
| Logistic Regression | 0.9486 | 0.9491 | 0.9489 | 0.947 | 0.9487 | 0.9485 | 0.0008 |
| Naive Bayes | 0.8824 | 0.8834 | 0.8825 | 0.8824 | 0.882 | 0.8825 | 0.0004 |
| Random Forest | 0.9979 | 0.998 | 0.9978 | 0.9979 | 0.9979 | 0.9979 | 0.0001 |

---

### Metrics of Trained Models on CIC-IDS-2017

| **Classifier** | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1-Score** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.8858 | 0.1758 | 0.8097 | 0.8858 | 0.8435 |
| K-Nearest Neighbors | 0.9979 | 0.8145 | 0.9979 | 0.9979 | 0.9979 |
| Linear Discriminant Analysis | 0.9052 | 0.5839 | 0.9322 | 0.9052 | 0.9148 |
| Logistic Regression | 0.9474 | 0.3612 | 0.9471 | 0.9474 | 0.945 |
| Naive Bayes | 0.8823 | 0.2027 | 0.8536 | 0.8823 | 0.8635 |
| Random Forest | 0.998 | 0.825 | 0.9979 | 0.998 | 0.9979 |

---

### Accuracies of Each Class in CIC-IDS-2017

| **Class** | **AdaBoost** | **K-Nearest Neighbors** | **Linear Discriminant Analysis** | **Logistic Regression** | **Naive Bayes** | **Random Forest** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| BENIGN | 0.99225 | 0.998753 | 0.935687 | 0.97476 | 0.963795 | 0.999275 |
| Bot | 0 | 0.753043 | 0.008696 | 0 | 0 | 0.476522 |
| DDoS | 0 | 0.997731 | 0.567035 | 0.718008 | 0.466222 | 0.999583 |
| DoS GoldenEye | 0.000961 | 0.994234 | 0.771941 | 0.611467 | 0.075913 | 0.994555 |
| DoS Hulk | 0.893971 | 0.996619 | 0.797276 | 0.8787 | 0.816523 | 0.993469 |
| DoS Slowhttptest | 0 | 0.980964 | 0.749365 | 0.729061 | 0.196066 | 0.989213 |
| DoS slowloris | 0 | 0.986553 | 0.330073 | 0.521394 | 0.521394 | 0.992054 |
| FTP-Patator | 0 | 0.992605 | 0.644482 | 0 | 0 | 0.997156 |
| Heartbleed | 0 | 0.8 | 1 | 0 | 0 | 0.8 |
| Infiltration | 0.75 | 0.25 | 0.25 | 0 | 0 | 0.75 |
| PortScan | 0 | 0.999525 | 0.987175 | 0.984727 | 0 | 0.999415 |
| SSH-Patator | 0 | 0.964803 | 0.913043 | 0 | 0 | 0.931677 |
| Web Attack - Brute Force | 0 | 0.754464 | 0.803571 | 0 | 0 | 0.71875 |
| Web Attack - Sql Injection | 0 | 0.4 | 0 | 0 | 0 | 0.4 |
| Web Attack - XSS | 0 | 0.348259 | 0 | 0 | 0 | 0.333333 |

---

## Binary

### Cross-Validation Results for CIC-IDS-2017

| **Classifier** | **Score1** | **Score2** | **Score3** | **Score4** | **Score5** | **Mean** | **Standard Deviation** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.9895 | 0.9914 | 0.9901 | 0.9889 | 0.9876 | 0.9895 | 0.0013 |
| K-Nearest Neighbors | 0.9982 | 0.9984 | 0.9983 | 0.9983 | 0.9983 | 0.9983 | 0.0001 |
| Linear Discriminant Analysis | 0.9239 | 0.9245 | 0.9237 | 0.9232 | 0.9231 | 0.9237 | 0.0005 |
| Logistic Regression | 0.9448 | 0.9438 | 0.9431 | 0.9426 | 0.9433 | 0.9435 | 0.0007 |
| Naive Bayes | 0.8872 | 0.8882 | 0.8876 | 0.8872 | 0.8872 | 0.8875 | 0.0004 |
| Random Forest | 0.9983 | 0.9983 | 0.9982 | 0.9982 | 0.9982 | 0.9982 | 0.0001 |

---

### Metrics for Trained Models on CIC-IDS-2017

| **Classifier** | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1-Score** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.9918 | 0.9824 | 0.9918 | 0.9918 | 0.9918 |
| K-Nearest Neighbors | 0.9234 | 0.7857 | 0.9254 | 0.9234 | 0.9155 |
| Linear Discriminant Analysis | 0.9436 | 0.8863 | 0.9424 | 0.9436 | 0.9428 |
| Logistic Regression | 0.8872 | 0.7565 | 0.8799 | 0.8872 | 0.8816 |
| Naive Bayes | 0.9984 | 0.9966 | 0.9984 | 0.9984 | 0.9984 |
| Random Forest | 0.9984 | 0.9977 | 0.9984 | 0.9984 | 0.9984 |

---

### Accuracies for Attack and Normal Classes on CIC-IDS-2017

| **Classifier** | **attack** | **normal** |
|:---:|:---:|:---:|
| AdaBoost | 0.96822 | 0.996615 |
| K-Nearest Neighbors | 0.577487 | 0.993876 |
| Linear Discriminant Analysis | 0.799691 | 0.972916 |
| Logistic Regression | 0.558825 | 0.954149 |
| Naive Bayes | 0.993972 | 0.999256 |
| Random Forest | 0.996689 | 0.998743 |

---

# NSL-KDD-2009

## Multiclass

### Cross-Validation Results of NSL-KDD-2009

| **Classifier** | **Score1** | **Score2** | **Score3** | **Score4** | **Score5** | **Mean** | **Standard Deviation** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.6091 | 0.8034 | 0.6834 | 0.6848 | 0.8421 | 0.7246 | 0.0856 |
| Gradient Boosting | 0.9889 | 0.9886 | 0.9897 | 0.9903 | 0.9894 | 0.9894 | 0.0006 |
| K-Nearest Neighbors | 0.9895 | 0.9885 | 0.9907 | 0.9892 | 0.9891 | 0.9894 | 0.0007 |
| Linear Discriminant Analysis | 0.9291 | 0.929 | 0.9326 | 0.9304 | 0.9278 | 0.9298 | 0.0016 |
| Logistic Regression | 0.9599 | 0.9583 | 0.9629 | 0.9613 | 0.9581 | 0.9601 | 0.0018 |
| Naive Bayes | 0.8132 | 0.8149 | 0.816 | 0.8152 | 0.814 | 0.8147 | 0.001 |
| Random Forest | 0.994 | 0.9934 | 0.9944 | 0.994 | 0.9934 | 0.9938 | 0.0004 |

---

### Metrics of Trained Models on NSL-KDD-2009

| **Classifier** | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1-Score** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.7853 | 0.6317 | 0.8165 | 0.7853 | 0.7913 |
| Gradient Boosting | 0.9892 | 0.8436 | 0.9891 | 0.9892 | 0.989 |
| K-Nearest Neighbors | 0.9901 | 0.8608 | 0.99 | 0.9901 | 0.99 |
| Linear Discriminant Analysis | 0.9278 | 0.8075 | 0.9308 | 0.9278 | 0.929 |
| Logistic Regression | 0.9599 | 0.7887 | 0.9594 | 0.9599 | 0.9592 |
| Naive Bayes | 0.8143 | 0.6458 | 0.866 | 0.8143 | 0.8233 |
| Random Forest | 0.9933 | 0.842 | 0.9932 | 0.9933 | 0.9932 |

---

### Accuracies of Each Class in NSL-KDD-2009

| **Class** | **AdaBoost** | **Gradient Boosting** | **K-Nearest Neighbors** | **Linear Discriminant Analysis** | **Logistic Regression** | **Naive Bayes** | Random Forest |
|:---:|---|---|---|---|---|---|---|
| dos | 0.914982 | 0.99857 | 0.997761 | 0.944275 | 0.962435 | 0.698053 | 0.998507 |
| normal | 0.750238 | 0.994156 | 0.991429 | 0.941347 | 0.97866 | 0.909618 | 0.995412 |
| probe | 0.578185 | 0.971042 | 0.985521 | 0.844353 | 0.936535 | 0.898166 | 0.989624 |
| r2l | 0.446205 | 0.848207 | 0.891576 | 0.744787 | 0.659716 | 0.254379 | 0.914095 |
| u2r | 0.46875 | 0.40625 | 0.4375 | 0.5625 | 0.40625 | 0.46875 | 0.3125 |

---

## Binary

### Cross-Validation Results for NSL-KDD-2009

| **Classifier** | **Score1** | **Score2** | **Score3** | **Score4** | **Score5** | **Mean** | **Standard Deviation** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.9628 | 0.964 | 0.9641 | 0.9648 | 0.9639 | 0.9639 | 0.0006 |
| K-Nearest Neighbors | 0.9905 | 0.9895 | 0.9912 | 0.9899 | 0.9898 | 0.9902 | 0.0006 |
| Linear Discriminant Analysis | 0.9323 | 0.9328 | 0.935 | 0.935 | 0.9312 | 0.9332 | 0.0015 |
| Logistic Regression | 0.9494 | 0.9497 | 0.9522 | 0.9545 | 0.9479 | 0.9507 | 0.0024 |
| Naive Bayes | 0.8759 | 0.8758 | 0.8779 | 0.8758 | 0.8746 | 0.876 | 0.0011 |
| Random Forest | 0.9944 | 0.994 | 0.9941 | 0.9947 | 0.9937 | 0.9942 | 0.0003 |

---

### Metrics for Trained Models on NSL-KDD-2009

| **Classifier** | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1-Score** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.9638 | 0.9636 | 0.9638 | 0.9638 | 0.9638 |
| K-Nearest Neighbors | 0.991 | 0.991 | 0.991 | 0.991 | 0.991 |
| Linear Discriminant Analysis | 0.932 | 0.9309 | 0.933 | 0.932 | 0.9319 |
| Logistic Regression | 0.9503 | 0.9499 | 0.9504 | 0.9503 | 0.9503 |
| Naive Bayes | 0.8767 | 0.8744 | 0.8811 | 0.8767 | 0.876 |
| Random Forest | 0.994 | 0.9939 | 0.994 | 0.994 | 0.994 |

---

### Accuracies for Attack and Normal Classes on NSL-KDD-2009

| **Classifier** | **attack** | **normal** |
|:---:|:---:|:---:|
| AdaBoost | 0.958236 | 0.96892 |
| K-Nearest Neighbors | 0.990818 | 0.99117 |
| Linear Discriminant Analysis | 0.902955 | 0.958921 |
| Logistic Regression | 0.938333 | 0.961432 |
| Naive Bayes | 0.813228 | 0.935633 |
| Random Forest | 0.992962 | 0.994892 |

---

# UNSW-NB15

## Multiclass

### Cross-Validation Results of UNSW-NB15

| **Classifier** | **Score1** | **Score2** | **Score3** | **Score4** | **Score5** | **Mean** | **Standard Deviation** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.8656 | 0.8707 | 0.7376 | 0.8704 | 0.8702 | 0.8429 | 0.0527 |
| K-Nearest Neighbors | 0.9726 | 0.9724 | 0.973 | 0.9727 | 0.9724 | 0.9726 | 0.0002 |
| Linear Discriminant Analysis | 0.9611 | 0.959 | 0.9609 | 0.9608 | 0.9604 | 0.9604 | 0.0008 |
| Logistic Regression | 0.9732 | 0.9733 | 0.974 | 0.9731 | 0.9732 | 0.9734 | 0.0003 |
| Naive Bayes | 0.8694 | 0.8713 | 0.8689 | 0.8694 | 0.8697 | 0.8697 | 0.0008 |
| Random Forest | 0.9812 | 0.9811 | 0.9818 | 0.9815 | 0.9813 | 0.9814 | 0.0003 |

---

### Metrics of Trained Models on UNSW-NB15

| **Classifier** | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1-Score** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.8556 | 0.2562 | 0.9498 | 0.8556 | 0.8933 |
| K-Nearest Neighbors | 0.9816 | 0.4871 | 0.9826 | 0.9816 | 0.9818 |
| Linear Discriminant Analysis | 0.9615 | 0.4897 | 0.9752 | 0.9615 | 0.9669 |
| Logistic Regression | 0.9746 | 0.3137 | 0.9729 | 0.9746 | 0.9718 |
| Naive Bayes | 0.9464 | 0.1942 | 0.9364 | 0.9464 | 0.9374 |
| Random Forest | 0.9897 | 0.5835 | 0.9904 | 0.9897 | 0.9891 |

---

### Accuracies of Each Class in UNSW-NB15

| **Class** | **AdaBoost** | **K-Nearest Neighbors** | **Linear Discriminant Analysis** | **Logistic Regression** | **Naive Bayes** | **Random Forest** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Analysis | 0 | 0.214497 | 0.025148 | 0.005917 | 0 | 0.121302 |
| Backdoor | 0 | 0.163498 | 0.072243 | 0 | 0 | 0.140684 |
| Backdoors | 0 | 0.268817 | 0.731183 | 0 | 0 | 0.129032 |
| DoS | 0 | 0.430147 | 0.235907 | 0.001838 | 0.330882 | 0.504902 |
| Exploits | 0.73927 | 0.815718 | 0.581619 | 0.761384 | 0.017834 | 0.946499 |
| Fuzzers | 0.013105 | 0.568175 | 0.662559 | 0.3 | 0.008424 | 0.734477 |
| Generic | 0.783142 | 0.840162 | 0.78536 | 0.790188 | 0.796712 | 0.911665 |
| Normal | 0.876032 | 0.996239 | 0.983236 | 0.995693 | 0.982845 | 0.998876 |
| Reconnaissance | 0.314386 | 0.671781 | 0.006036 | 0.595825 | 0 | 0.789235 |
| Shellcode | 0 | 0.314732 | 0.488839 | 0 | 0 | 0.808036 |
| Worms | 0.092593 | 0.074074 | 0.814815 | 0 | 0 | 0.333333 |

---

## Binary

### Cross-Validation Results for UNSW-NB15

| **Classifier** | **Score1** | **Score2** | **Score3** | **Score4** | **Score5** | **Mean** | **Standard Deviation** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.9903 | 0.9898 | 0.9901 | 0.9902 | 0.9905 | 0.9902 | 0.0002 |
| K-Nearest Neighbors | 0.9886 | 0.9886 | 0.9884 | 0.9883 | 0.9886 | 0.9885 | 0.0001 |
| Linear Discriminant Analysis | 0.9838 | 0.9838 | 0.9843 | 0.9836 | 0.9838 | 0.9838 | 0.0002 |
| Logistic Regression | 0.9862 | 0.9862 | 0.9865 | 0.986 | 0.9861 | 0.9862 | 0.0002 |
| Naive Bayes | 0.9588 | 0.9583 | 0.9581 | 0.9584 | 0.958 | 0.9583 | 0.0003 |
| Random Forest | 0.9931 | 0.9926 | 0.9926 | 0.9926 | 0.9928 | 0.9927 | 0.0002 |

---

### Metrics for Trained Models on UNSW-NB15

| **Classifier** | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1-Score** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| AdaBoost | 0.9903 | 0.9425 | 0.9902 | 0.9903 | 0.9902 |
| K-Nearest Neighbors | 0.9888 | 0.9372 | 0.9888 | 0.9888 | 0.9888 |
| Linear Discriminant Analysis | 0.9839 | 0.9887 | 0.9878 | 0.9839 | 0.985 |
| Logistic Regression | 0.9865 | 0.9689 | 0.9881 | 0.9865 | 0.987 |
| Naive Bayes | 0.9583 | 0.7162 | 0.9538 | 0.9583 | 0.9555 |
| Random Forest | 0.9931 | 0.96 | 0.9931 | 0.9931 | 0.9931 |

---

### Accuracies for Attack and Normal Classes on UNSW-NB15

| **Classifier** | **attack** | **normal** |
|:---:|:---:|:---:|
| AdaBoost | 0.889528 | 0.995404 |
| K-Nearest Neighbors | 0.879993 | 0.994338 |
| Linear Discriminant Analysis | 0.993944 | 0.983427 |
| Logistic Regression | 0.949348 | 0.988388 |
| Naive Bayes | 0.44831 | 0.984177 |
| Random Forest | 0.923319 | 0.996692 |

---