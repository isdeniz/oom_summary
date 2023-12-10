import subprocess
import os
import zipfile
import shutil
import pandas as pd
import numpy as np

outputs = os.listdir('/Users/isdeniz/Downloads/analysis7-14')
print(len(outputs))

typeMetricsSummary = pd.DataFrame()

for fname in outputs:
    if fname.endswith('-out'):
        path = '/Users/isdeniz/Documents/analysis-example/' + fname + '/' + 'typeMetrics.csv'
        typeMetrics = pd.read_csv(f'{path}')
        temp = fname[:-4]
        if fname.startswith('neo4j'):
            repository_name = 'neo4j/neo4j'
            release = temp.split("-",1)[1]
        elif fname.startswith('pinpoint'):
            repository_name = 'pinpoint-apm/pinpoint'
            release = temp.split("-",1)[1]
        elif fname.startswith('nacos'):
            repository_name = 'alibaba/nacos'
            release = temp.split("-",1)[1]
        elif fname.startswith('openapi'):
            repository_name = 'OpenAPITools/openapi-generator'
            release = temp.split("-",3)[2]
        elif fname.startswith('shardingsphere'):
            repository_name = 'apache/shardingsphere'
            release = temp.split("-",1)[1]
        elif fname.startswith('druid'):
            repository_name = 'apache/druid'
            release = temp.split("-",2)[2]
        elif fname.startswith('thingsboard'):
            repository_name = 'thingsboard/thingsboard'
            release = temp.split("-",1)[1]
        elif fname.startswith('skywalking'):
            repository_name = 'apache/skywalking'
            release = temp.split("-",1)[1]
        elif fname.startswith('pulsar'):
            repository_name = 'apache/pulsar'
            release = temp.split("-",1)[1]
        elif fname.startswith('questdb'):
            repository_name = 'questdb/questdb'
            release = temp.split("-",1)[1]
        elif fname.startswith('zipkin'):
            repository_name = 'openzipkin/zipkin'
            release = temp.split("-",1)[1]
        elif fname.startswith('selenium'):
            repository_name = 'SeleniumHQ/selenium'
            release = temp.split("-",1)[1]
        elif fname.startswith('jedis'):
            repository_name = 'redis/jedis'
            release = temp.split("-",1)[1]
        elif fname.startswith('dubbo'):
            repository_name = 'apache/dubbo'
            release = temp.split("-",1)[1]
        elif fname.startswith('spring-boot-admin'):
            repository_name = 'codecentric/spring-boot-admin'
            release = temp.split("-",3)[3]
        elif fname.startswith('logstash'):
            repository_name = 'elastic/logstash'
            release = temp.split("-",1)[1]
        elif fname.startswith('halo'):
            repository_name = 'halo-dev/halo'
            release = temp.split("-",1)[1]
        elif fname.startswith('NewPipe'):
            repository_name = 'TeamNewPipe/NewPipe'
            release = temp.split("-",1)[1]
        elif fname.startswith('jib'):
            repository_name = 'GoogleContainerTools/jib'
            release = temp.split("-",1)[1]
        elif fname.startswith('grpc'):
            repository_name = 'grpc/grpc-java'
            release = temp.split("-",2)[2]
        elif fname.startswith('Mindustry'):
            repository_name = 'Anuken/Mindustry'
            release = temp.split("-",1)[1]
        elif fname.startswith('RxJava'):
            repository_name = 'ReactiveX/RxJava'
            release = temp.split("-",1)[1]
        elif fname.startswith('dbeaver'):
            repository_name = 'dbeaver/dbeaver'
            release = temp.split("-",1)[1]
        elif fname.startswith('react'):
            repository_name = 'facebook/react-native'
            release = temp.split("-",3)[2]
        elif fname.startswith('spring-boot'):
            repository_name = 'spring-projects/spring-boot'
            release = temp.split("-",3)[2]
        elif fname.startswith('mockito'):
            repository_name = 'mockito/mockito'
            release = temp.split("-",1)[1]
        elif fname.startswith('spring-framework'):
            repository_name = 'spring-projects/spring-framework'
            release = temp.split("-",2)[2]
        elif fname.startswith('quarkus'):
            repository_name = 'quarkusio/quarkus'
            release = temp.split("-",1)[1]
        elif fname.startswith('conductor'):
            repository_name = 'Netflix/conductor'
            release = temp.split("-",1)[1]
        elif fname.startswith('zaproxy'):
            repository_name = 'zaproxy/zaproxy'
            release = temp.split("-",1)[1]
        if typeMetrics.shape[0] == 0:
            typeMetricsSummary.loc[0,'NOF_min'] = np.NAN
            typeMetricsSummary.loc[0,'NOF_max'] = np.NAN
            typeMetricsSummary.loc[0,'NOF_sum'] = np.NAN
            typeMetricsSummary.loc[0,'NOPF_min'] = np.NAN
            typeMetricsSummary.loc[0,'NOPF_max'] = np.NAN
            typeMetricsSummary.loc[0,'NOPF_sum'] = np.NAN
            typeMetricsSummary.loc[0,'NOM_min'] = np.NAN
            typeMetricsSummary.loc[0,'NOM_max'] = np.NAN
            typeMetricsSummary.loc[0,'NOM_sum'] = np.NAN
            typeMetricsSummary.loc[0,'NOPM_min'] = np.NAN
            typeMetricsSummary.loc[0,'NOPM_max'] = np.NAN
            typeMetricsSummary.loc[0,'NOPM_sum'] = np.NAN
            typeMetricsSummary.loc[0,'LOC_min'] = np.NAN
            typeMetricsSummary.loc[0,'LOC_max'] = np.NAN
            typeMetricsSummary.loc[0,'LOC_sum'] = np.NAN
            typeMetricsSummary.loc[0,'WMC_min'] = np.NAN
            typeMetricsSummary.loc[0,'WMC_max'] = np.NAN
            typeMetricsSummary.loc[0,'WMC_sum'] = np.NAN
            typeMetricsSummary.loc[0,'NC_min'] = np.NAN
            typeMetricsSummary.loc[0,'NC_max'] = np.NAN
            typeMetricsSummary.loc[0,'NC_sum'] = np.NAN
            typeMetricsSummary.loc[0,'DIT_min'] = np.NAN
            typeMetricsSummary.loc[0,'DIT_max'] = np.NAN
            typeMetricsSummary.loc[0,'DIT_sum'] = np.NAN
            typeMetricsSummary.loc[0,'LCOM_min'] = np.NAN
            typeMetricsSummary.loc[0,'LCOM_max'] = np.NAN
            typeMetricsSummary.loc[0,'LCOM_sum'] = np.NAN
            typeMetricsSummary.loc[0,'FANIN_min'] = np.NAN
            typeMetricsSummary.loc[0,'FANIN_max'] = np.NAN
            typeMetricsSummary.loc[0,'FANIN_sum'] = np.NAN
            typeMetricsSummary.loc[0,'FANOUT_min'] = np.NAN
            typeMetricsSummary.loc[0,'FANOUT_max'] = np.NAN
            typeMetricsSummary.loc[0,'FANOUT_sum'] = np.NAN
            typeMetricsSummary.loc[0,'type_count'] = np.NAN
        else:
            typeMetricsSummary.loc[0,'NOF_min'] = typeMetrics['NOF'].min()
            typeMetricsSummary.loc[0,'NOF_max'] = typeMetrics['NOF'].max()
            typeMetricsSummary.loc[0,'NOF_sum'] = typeMetrics['NOF'].sum()
            typeMetricsSummary.loc[0,'NOPF_min'] = typeMetrics['NOPF'].min()
            typeMetricsSummary.loc[0,'NOPF_max'] = typeMetrics['NOPF'].max()
            typeMetricsSummary.loc[0,'NOPF_sum'] = typeMetrics['NOPF'].sum()
            typeMetricsSummary.loc[0,'NOM_min'] = typeMetrics['NOM'].min()
            typeMetricsSummary.loc[0,'NOM_max'] = typeMetrics['NOM'].max()
            typeMetricsSummary.loc[0,'NOM_sum'] = typeMetrics['NOM'].sum()
            typeMetricsSummary.loc[0,'NOPM_min'] = typeMetrics['NOPM'].min()
            typeMetricsSummary.loc[0,'NOPM_max'] = typeMetrics['NOPM'].max()
            typeMetricsSummary.loc[0,'NOPM_sum'] = typeMetrics['NOPM'].sum()
            typeMetricsSummary.loc[0,'LOC_min'] = typeMetrics['LOC'].min()
            typeMetricsSummary.loc[0,'LOC_max'] = typeMetrics['LOC'].max()
            typeMetricsSummary.loc[0,'LOC_sum'] = typeMetrics['LOC'].sum()
            typeMetricsSummary.loc[0,'WMC_min'] = typeMetrics['WMC'].min()
            typeMetricsSummary.loc[0,'WMC_max'] = typeMetrics['WMC'].max()
            typeMetricsSummary.loc[0,'WMC_sum'] = typeMetrics['WMC'].sum()
            typeMetricsSummary.loc[0,'NC_min'] = typeMetrics['NC'].min()
            typeMetricsSummary.loc[0,'NC_max'] = typeMetrics['NC'].max()
            typeMetricsSummary.loc[0,'NC_sum'] = typeMetrics['NC'].sum()
            typeMetricsSummary.loc[0,'DIT_min'] = typeMetrics['DIT'].min()
            typeMetricsSummary.loc[0,'DIT_max'] = typeMetrics['DIT'].max()
            typeMetricsSummary.loc[0,'DIT_sum'] = typeMetrics['DIT'].sum()
            typeMetricsSummary.loc[0,'LCOM_min'] = typeMetrics['LCOM'].min()
            typeMetricsSummary.loc[0,'LCOM_max'] = typeMetrics['LCOM'].max()
            typeMetricsSummary.loc[0,'LCOM_sum'] = typeMetrics['LCOM'].sum()
            typeMetricsSummary.loc[0,'FANIN_min'] = typeMetrics['FANIN'].min()
            typeMetricsSummary.loc[0,'FANIN_max'] = typeMetrics['FANIN'].max()
            typeMetricsSummary.loc[0,'FANIN_sum'] = typeMetrics['FANIN'].sum()
            typeMetricsSummary.loc[0,'FANOUT_min'] = typeMetrics['FANOUT'].min()
            typeMetricsSummary.loc[0,'FANOUT_max'] = typeMetrics['FANOUT'].max()
            typeMetricsSummary.loc[0,'FANOUT_sum'] = typeMetrics['FANOUT'].sum()
            typeCount = typeMetrics.groupby(['Project Name'])['Type Name'].nunique().reset_index()
            typeMetricsSummary.loc[0,'type_count'] = typeCount['Type Name'].sum()
        typeMetricsSummary.loc[0,'repository_name'] = repository_name
        typeMetricsSummary.loc[0,'release'] = release
        typeMetricsSummary.loc[0,'info'] = temp
        typeMetricsSummary.to_csv('/Users/isdeniz/Documents/results/typeMetricsSummary.csv',mode='a',index=False,header=False) 