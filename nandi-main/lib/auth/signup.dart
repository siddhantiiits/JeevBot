import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter_overlay_loader/flutter_overlay_loader.dart';
import 'package:nandi/auth/login.dart';
import 'package:sizer/sizer.dart';

import '../constants.dart';
import '../home_portal.dart';
import '../screens/new_user/new_profile.dart';
import '../utils/RoundedButton.dart';

class SignUpPage extends StatefulWidget {
  const SignUpPage({Key? key}) : super(key: key);

  @override
  _SignUpPageState createState() => _SignUpPageState();
}

class _SignUpPageState extends State<SignUpPage> {
  final firstNameController = TextEditingController();
  final lastNameController = TextEditingController();
  final stateController = TextEditingController();
  final cityController = TextEditingController();
  final pincodeController = TextEditingController();
  final passwordController = TextEditingController();
  final usernameController = TextEditingController();
  final addressController = TextEditingController();
  final phoneController = TextEditingController();
  final registrationNumberController = TextEditingController();

  final formGlobalKey = GlobalKey<FormState>();
  bool _obscureText = true;
  bool agree = false;
  String dropdownValue = "Boarders";

  void signup() async {
    try {
      Loader.show(context, progressIndicator: CircularProgressIndicator());
      UserCredential userCredential = await FirebaseAuth.instance
          .createUserWithEmailAndPassword(
              email: usernameController.value.text + "@nandiuser.com",
              password: passwordController.value.text);
      print(userCredential.user?.uid);
      await FirebaseFirestore.instance
          .collection('Users')
          .doc(userCredential.user?.uid)
          .set({
        'first-name': firstNameController.value.text,
        'last-name': lastNameController.value.text,
        'state': stateController.value.text,
        'city': cityController.value.text,
        'pincode': pincodeController.value.text,
        'address': addressController.value.text,
        'phone': phoneController.value.text,
        'reg_number': "XX001",
        'role': dropdownValue,
        'regNo': registrationNumberController.value.text,
      });
      Loader.hide();
      Navigator.pushReplacement(
          context,
          MaterialPageRoute(
              builder: (context) => NewProfile(
                    uid: userCredential.user?.uid,
                  )));
    } on FirebaseAuthException catch (e) {
      Loader.hide();
      if (e.code == 'weak-password') {
        print('The password provided is too weak.');
      } else if (e.code == 'email-already-in-use') {
        print('The account already exists for that email.');
      }
    } catch (e) {
      print(e);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF004AAD),
      body: Column(
        children: [
          Container(
              height: 35.h, child: Image.asset('assets/images/nandi-logo.png')),
          Expanded(
            child: Container(
              padding: EdgeInsets.only(left: 4.w, right: 4.w, top: 4.h),
              width: 100.w,
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(10.w),
                  topRight: Radius.circular(10.w),
                ),
              ),
              child: SingleChildScrollView(
                child: Form(
                  key: formGlobalKey,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      Text(
                        "Partner Registration",
                        style: TextStyle(
                          fontSize: 20.sp,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      SizedBox(
                        height: 3.h,
                      ),
                      Row(
                        children: [
                          Flexible(
                            child: TextFormField(
                              decoration: authTextFieldDecoration.copyWith(
                                labelText: "First Name",
                                hintText: "Enter your First Name",
                              ),
                              validator: (value) {
                                if (value!.isEmpty) {
                                  return 'Please enter value';
                                }
                                return null;
                              },
                              controller: firstNameController,
                              keyboardType: TextInputType.name,
                            ),
                          ),
                          SizedBox(width: 2.w),
                          Flexible(
                            child: TextFormField(
                              decoration: authTextFieldDecoration.copyWith(
                                labelText: "Last Name",
                                hintText: "Enter your last name",
                              ),
                              validator: (value) {
                                if (value!.isEmpty) {
                                  return 'Please enter value';
                                }
                                return null;
                              },
                              controller: lastNameController,
                              keyboardType: TextInputType.name,
                            ),
                          ),
                        ],
                      ),
                      SizedBox(
                        height: 1.5.h,
                      ),
                      TextFormField(
                        maxLength: 10,
                        decoration: authTextFieldDecoration.copyWith(
                          labelText: "Phone Number",
                          hintText: "Enter your number",
                        ),
                        validator: (value) {
                          if (value!.isEmpty) {
                            return 'Please enter value';
                          }
                          return null;
                        },
                        controller: phoneController,
                        keyboardType: TextInputType.number,
                      ),
                      SizedBox(
                        height: 1.5.h,
                      ),
                      Row(
                        children: [
                          Flexible(
                            child: TextFormField(
                              decoration: authTextFieldDecoration.copyWith(
                                labelText: "State",
                                hintText: "Enter your State",
                              ),
                              validator: (value) {
                                if (value!.isEmpty) {
                                  return 'Please enter value';
                                }
                                return null;
                              },
                              controller: stateController,
                              keyboardType: TextInputType.name,
                            ),
                          ),
                          SizedBox(width: 1.w),
                          Flexible(
                            child: TextFormField(
                              decoration: authTextFieldDecoration.copyWith(
                                labelText: "City",
                                hintText: "Enter your city",
                              ),
                              validator: (value) {
                                if (value!.isEmpty) {
                                  return 'Please enter value';
                                }
                                return null;
                              },
                              controller: cityController,
                              keyboardType: TextInputType.name,
                            ),
                          ),
                          SizedBox(width: 1.w),
                          Flexible(
                            child: TextFormField(
                              decoration: authTextFieldDecoration.copyWith(
                                labelText: "Pincode",
                                hintText: "Enter your pincode",
                              ),
                              validator: (value) {
                                if (value!.isEmpty) {
                                  return 'Please enter value';
                                }
                                return null;
                              },
                              controller: pincodeController,
                              keyboardType: TextInputType.number,
                            ),
                          ),
                        ],
                      ),
                      SizedBox(
                        height: 1.5.h,
                      ),
                      TextFormField(
                        decoration: authTextFieldDecoration.copyWith(
                          labelText: "Address",
                          hintText: "Enter your address",
                        ),
                        validator: (value) {
                          if (value!.isEmpty) {
                            return 'Please enter value';
                          }
                          return null;
                        },
                        controller: addressController,
                        keyboardType: TextInputType.name,
                      ),
                      SizedBox(
                        height: 1.5.h,
                      ),
                      TextFormField(
                        decoration: authTextFieldDecoration.copyWith(
                          labelText: "Username",
                          hintText: "Enter your username",
                        ),
                        validator: (value) {
                          if (value!.isEmpty) {
                            return 'Please enter value';
                          }
                          return null;
                        },
                        controller: usernameController,
                        keyboardType: TextInputType.name,
                      ),
                      SizedBox(
                        height: 1.5.h,
                      ),
                      TextFormField(
                        decoration: authTextFieldDecoration.copyWith(
                          labelText: "Registration Number",
                          hintText: "Enter your Registration Number",
                        ),
                        validator: (value) {
                          if (value!.isEmpty) {
                            return 'Please enter value';
                          }
                          return null;
                        },
                        controller: registrationNumberController,
                        keyboardType: TextInputType.name,
                      ),
                      SizedBox(
                        height: 1.5.h,
                      ),
                      TextFormField(
                        controller: passwordController,
                        textAlign: TextAlign.center,
                        obscureText: _obscureText,
                        validator: (value) {
                          if (value!.isEmpty) {
                            return 'Please enter value';
                          }
                          return null;
                        },
                        decoration: authTextFieldDecoration.copyWith(
                          labelText: "Password",
                          hintText: "Enter your Password",
                          suffixIcon: IconButton(
                            icon: Icon(_obscureText
                                ? Icons.visibility_off
                                : Icons.visibility),
                            onPressed: () {
                              setState(() {
                                _obscureText = !_obscureText;
                              });
                            },
                          ),
                        ),
                      ),
                      SizedBox(
                        height: 1.5.h,
                      ),
                      DropdownButton<String>(
                        icon: const Icon(Icons.arrow_drop_down),
                        hint: Text(dropdownValue),
                        iconSize: 24,
                        elevation: 16,
                        style: const TextStyle(color: Colors.black),
                        underline: Container(
                          height: 2,
                          color: Colors.blueGrey,
                        ),
                        onChanged: (String? newValue) {
                          setState(() {
                            dropdownValue = newValue!;
                          });
                        },
                        items: <String>[
                          'Boarders',
                          'Para-Veterinarians',
                          'Veterinarians',
                          'Others'
                        ].map<DropdownMenuItem<String>>((String value) {
                          return DropdownMenuItem<String>(
                            value: value,
                            child: Text(value),
                          );
                        }).toList(),
                      ),
                      Column(
                        children: [
                          Align(
                            alignment: Alignment.centerLeft,
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.start,
                              children: [
                                Transform.scale(
                                  scale: 0.23.w,
                                  child: Checkbox(
                                    activeColor: Color(0xFF004AAD),
                                    value: agree,
                                    onChanged: (value) {
                                      setState(() {
                                        agree = !agree;
                                      });
                                    },
                                  ),
                                ),
                                Flexible(
                                  child: Text(
                                    "I have read and accept terms and conditions",
                                    style: TextStyle(fontSize: 10.sp),
                                    maxLines: 2,
                                    overflow: TextOverflow.ellipsis,
                                  ),
                                ),
                              ],
                            ),
                          ),
                          Align(
                            alignment: Alignment.center,
                            child: RoundedButton(
                              color: agree ? Color(0xFF004AAD) : Colors.grey,
                              onPressed: () {
                                if (formGlobalKey.currentState!.validate()) {
                                  formGlobalKey.currentState!.save();
                                  if (agree) {
                                    signup();
                                  }
                                }
                              },
                              text: "Sign Up",
                            ),
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Text(
                                "Already have an account? ",
                                style: TextStyle(fontSize: 11.sp),
                              ),
                              GestureDetector(
                                onTap: () {
                                  Navigator.pushReplacement(
                                      context,
                                      MaterialPageRoute(
                                          builder: (context) => LogInPage()));
                                },
                                child: Text(
                                  "Sign Up",
                                  style: TextStyle(
                                      color: Colors.lightBlueAccent,
                                      fontSize: 11.sp),
                                ),
                              ),
                            ],
                          ),
                          SizedBox(
                            height: 3.5.h,
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
