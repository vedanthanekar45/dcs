// Server.cpp
#include "Calculator.hh"
#include <omniORB4/omniORB.h>
#include <iostream>
#include <fstream>
using namespace std;

class Calculator_i : public POA_CalculatorApp::Calculator {
public:
  double add(double n1, double n2) {
    cout << "Received add request: " << n1 << " + " << n2 << std::endl;
    return n1 + n2;
  }
  double subtract(double n1, double n2) {
    cout << "Received subtract request: " << n1 << " - " << n2 << std::endl;
    return n1 - n2;
  }
};

int main(int argc, char** argv) {
  try {
    CORBA::ORB_var orb = CORBA::ORB_init(argc, argv);

    CORBA::Object_var obj = orb->resolve_initial_references("RootPOA");
    PortableServer::POA_var poa = PortableServer::POA::_narrow(obj);
    PortableServer::POAManager_var pman = poa->the_POAManager();
    pman->activate();

    Calculator_i* mycalculator = new Calculator_i();

    CORBA::Object_var mycalculator_obj = poa->servant_to_reference(mycalculator);

    CORBA::String_var ior = orb->object_to_string(mycalculator_obj);
    std::ofstream ofs("ior.txt");
    ofs << ior;
    ofs.close();
    cout << "Server is ready. IOR written to ior.txt" << std::endl;

    orb->run();
    orb->destroy();

  } catch (CORBA::Exception& e) {
    cerr << "Caught CORBA exception." << std::endl;
  }
  return 0;
}