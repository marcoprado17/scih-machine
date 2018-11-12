import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import csv

def generate_cpu_plot(file_service_name, service_name, rows, n_gps):
    i = 0

    x = []
    y = []

    for row in rows:
        x.append(i)
        y.append(float(row[4][0:4]))
        i += 1

    fig, ax = plt.subplots()
    fig.set_size_inches(13.5, 9.5)
    ax.plot(x, y)

    ax.set(xlabel='Indíce da amostra', ylabel='Percentual de CPU utilizada',
        title='Percentual de utilização da cpu pelo serviço: {} ({} dispositivos GPS)'.format(service_name, n_gps))
    ax.grid()

    fig.savefig("cpu_{}_{}.png".format(n_gps, file_service_name))
    plt.show()

def generate_mem_plot(file_service_name, service_name, rows, n_gps):
    i = 0

    x = []
    y = []

    for row in rows:
        x.append(i)
        y.append(float(row[7][0:4]))
        i += 1

    fig, ax = plt.subplots()
    fig.set_size_inches(13.5, 9.5)
    ax.plot(x, y)

    ax.set(xlabel='Indíce da amostra', ylabel='Percentual de memória utilizada',
        title='Percentual de utilização da memória pelo serviço: {} ({} dispositivos GPS)'.format(service_name, n_gps))
    ax.grid()

    fig.savefig("mem_{}_{}.png".format(n_gps, file_service_name))
    plt.show()

def get_total_row(row1, row2, row3, row4):
    cpu_total = float(row1[4][0:4]) + float(row2[4][0:4]) + float(row3[4][0:4]) + float(row4[4][0:4])
    cpu_total = "%.2f" % cpu_total + "%"
    mem_total = float(row1[7][0:4]) + float(row2[7][0:4]) + float(row3[7][0:4]) + float(row4[7][0:4])
    mem_total = "%.2f" % mem_total + "%"
    return ['', '', '', '', cpu_total, '', '', mem_total]

def generate_plots(file_name, n_gps):
    with open(file_name, 'r') as csvfile:
        rows = []
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            rows.append(row)
        
        gps_service_rows = []
        api_gateway_rows = []
        mongodb_rows = []
        ui_rows = []
        total_rows = []

        i = 0
        while i < len(rows):
            gps_service_rows.append(rows[i])
            api_gateway_rows.append(rows[i+1])
            mongodb_rows.append(rows[i+2])
            ui_rows.append(rows[i+3])
            total_rows.append(get_total_row(rows[i], rows[i+1], rows[i+2], rows[i+3]))
            i += 4

        generate_cpu_plot("gps-service", "GPS Service", gps_service_rows, n_gps)
        generate_cpu_plot("api-gateway", "API Gateway (sem verificar a assinatura)", api_gateway_rows, n_gps)
        generate_cpu_plot("mongodb", "MongoDB", mongodb_rows, n_gps)
        generate_cpu_plot("ui-server", "UI Server", ui_rows, n_gps)
        generate_cpu_plot("all-services", "Todos os serviços", total_rows, n_gps)

        generate_mem_plot("gps-service", "GPS Service", gps_service_rows, n_gps)
        generate_mem_plot("api-gateway", "API Gateway (sem verificar a assinatura)", api_gateway_rows, n_gps)
        generate_mem_plot("mongodb", "MongoDB", mongodb_rows, n_gps)
        generate_mem_plot("ui-server", "UI Server", ui_rows, n_gps)
        generate_mem_plot("all-services", "Todos os serviços", total_rows, n_gps)

# generate_plots("8x1.csv", 8)
# generate_plots("8x10.csv", 80)
# generate_plots("8x11.csv", 88)
# generate_plots("8x12.csv", 96)
# generate_plots("8x15.csv", 120)
generate_plots("without_sign_check.csv", "120")
