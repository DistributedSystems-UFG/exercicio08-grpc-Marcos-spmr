from __future__ import print_function
import logging
 
import grpc
import EmployeeService_pb2
import EmployeeService_pb2_grpc
 
import const
 
def run():
    with grpc.insecure_channel(const.IP + ':' + const.PORT) as channel:
        stub = EmployeeService_pb2_grpc.EmployeeServiceStub(channel)
        
        response = stub.GetEmployeeDataFromID(EmployeeService_pb2.EmployeeID(id=101))
        print('Employee\'s data: ' + str(response))
 
        response = stub.CreateEmployee(EmployeeService_pb2.EmployeeData(id=301, name='Jose da Silva', title='Programmer'))
        print('Added new employee ' + response.status)
 
        response = stub.UpdateEmployeeTitle(EmployeeService_pb2.EmployeeTitleUpdate(id=301, title='Senior Programmer'))
        print('Updated employee ' + response.status)
 
        response = stub.DeleteEmployee(EmployeeService_pb2.EmployeeID(id=201))
        print('Deleted employee ' + response.status)
 
        response = stub.ListAllEmployees(EmployeeService_pb2.EmptyMessage())
        print('All employees: ' + str(response))
 
        response = stub.GetEmployeesByTitle(EmployeeService_pb2.EmployeeTitle(title='Technical Leader'))
        print('Employees by title: ' + str(response))
 
        response = stub.CountEmployees(EmployeeService_pb2.EmptyMessage())
        print('Total employees: ' + str(response.count))
 
 
if __name__ == '__main__':
    logging.basicConfig()
    run()