import subprocess
import os
import zipfile
import shutil
import pandas as pd
import numpy as np

outputs = os.listdir('/Users/isdeniz/Downloads/analysis7-14')
print(len(outputs))

methodMetricsSummary = pd.DataFrame()

for fname in outputs:
    if fname.endswith('-out'):
        path = '/Users/isdeniz/Documents/analysis-example/' + fname + '/' + 'methodMetrics.csv'
        methodMetrics = pd.read_csv(f'{path}')
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
        if methodMetrics.shape[0] == 0:
            methodMetricsSummary.loc[0,'LOC_min'] = np.NAN
            methodMetricsSummary.loc[0,'LOC_max'] = np.NAN
            methodMetricsSummary.loc[0,'LOC_sum'] = np.NAN
            methodMetricsSummary.loc[0,'CC_min'] = np.NAN
            methodMetricsSummary.loc[0,'CC_max'] = np.NAN
            methodMetricsSummary.loc[0,'CC_sum'] = np.NAN
            methodMetricsSummary.loc[0,'PC_min'] = np.NAN
            methodMetricsSummary.loc[0,'PC_max'] = np.NAN
            methodMetricsSummary.loc[0,'PC_sum'] = np.NAN
            methodMetricsSummary.loc[0,'method_count'] = np.NAN
        else:
            methodMetricsSummary.loc[0,'LOC_min'] = methodMetrics['LOC'].min()
            methodMetricsSummary.loc[0,'LOC_max'] = methodMetrics['LOC'].max()
            methodMetricsSummary.loc[0,'LOC_sum'] = methodMetrics['LOC'].sum()
            methodMetricsSummary.loc[0,'CC_min'] = methodMetrics['CC'].min()
            methodMetricsSummary.loc[0,'CC_max'] = methodMetrics['CC'].max()
            methodMetricsSummary.loc[0,'CC_sum'] = methodMetrics['CC'].sum()
            methodMetricsSummary.loc[0,'PC_min'] = methodMetrics['PC'].min()
            methodMetricsSummary.loc[0,'PC_max'] = methodMetrics['PC'].max()
            methodMetricsSummary.loc[0,'PC_sum'] = methodMetrics['PC'].sum()
            methodCount = methodMetrics.groupby(['Package Name', 'Type Name'])['MethodName'].nunique().reset_index()
            methodMetricsSummary.loc[0,'method_count'] = methodCount['MethodName'].sum()
        methodMetricsSummary.loc[0,'repository_name'] = repository_name
        methodMetricsSummary.loc[0,'release'] = release
        methodMetricsSummary.loc[0,'info'] = temp
        methodMetricsSummary.to_csv('/Users/isdeniz/Documents/results/methodMetricsSummary.csv',mode='a',index=False,header=False) 