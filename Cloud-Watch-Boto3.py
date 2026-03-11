import boto3

# Create CloudWatch Client
cloudwatch = boto3.client('cloudwatch')

# # List alarms of insufficient data through the paginaion interface
# paginator = cloudwatch.get_paginator('describe_alarms')
# for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
#     print(response['MetricAlarms'])


# Create alarm
# cloudwatch.put_metric_alarm(
#     AlarmName='Web_Server_CPU_Utilization',
#     ComparisonOperator='GreaterThanThreshold',
#     EvaluationPeriods=1,
#     MetricName='CPUUtilization',
#     Namespace='AWS/EC2',
#     Period=60,
#     Statistic='Average',
#     Threshold=10.0,
#     ActionsEnabled=False,
#     AlarmDescription='Alarm when server CPU exceeds 10%',
#     Dimensions=[
#         {
#             'Name' : 'InstanceId',
#             'Value': 'i-08425ef4be6ec3f5e'
#         },
#     ],
#     Unit='Percent'
# )

# # Delete an alarm
# cloudwatch.delete_alarms(
#     AlarmNames=[
#         'Web_Server_CPU_Utilization'
#     ],
# )

# List metrics through the pagination interface
paginator = cloudwatch.get_paginator('list_metrics')
for response in paginator.paginate(Dimensions= [{'Name': 'LogGroupName'}], MetricName= 'IncomingLogEvents', Namespace='AWS/Logs'):
    print(response['Metrics'])