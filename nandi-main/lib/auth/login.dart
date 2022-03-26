import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter_overlay_loader/flutter_overlay_loader.dart';
import 'package:nandi/auth/signup.dart';
import 'package:nandi/home_portal.dart';
import 'package:nandi/utils/RoundedButton.dart';
import 'package:sizer/sizer.dart';
import '../constants.dart';
import '../screens/new_user/new_profile.dart';

class LogInPage extends StatefulWidget {
  const LogInPage({Key? key}) : super(key: key);

  @override
  State<LogInPage> createState() => _LogInPageState();
}

class _LogInPageState extends State<LogInPage> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  final formGlobalKey = GlobalKey<FormState>();
  bool _obscureText = true;

  Future<void> login() async {
    String email = emailController.value.text;
    if (!emailController.value.text.contains('@nandi.com')) {
      email = email + "@nandiuser.com";
    }
    try {
      Loader.show(context, progressIndicator: CircularProgressIndicator());
      await FirebaseAuth.instance.signInWithEmailAndPassword(
          email: email, password: passwordController.value.text);
      Loader.hide();
      if (email.contains('@nandiuser.com')) {
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(
            builder: (context) => NewProfile(
              uid: FirebaseAuth.instance.currentUser?.uid,
            ),
          ),
        );
      } else
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(
            builder: (context) => PortalHome(),
          ),
        );
    } on FirebaseAuthException catch (e) {
      Loader.hide();

      var snackBar = SnackBar(
        backgroundColor: Colors.red,
        content: Text(e.toString()),
      );
      ScaffoldMessenger.of(context).showSnackBar(snackBar);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF004AAD),
      body: Column(
        children: [
          Container(
              height: 40.h, child: Image.asset('assets/images/nandi-logo.png')),
          Expanded(
            child: Container(
              padding: EdgeInsets.only(left: 10.w, right: 10.w, top: 8.h),
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
                        "Welcome",
                        style: TextStyle(
                          fontSize: 20.sp,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      SizedBox(
                        height: 5.h,
                      ),
                      TextFormField(
                        decoration: authTextFieldDecoration.copyWith(
                          labelText: "Username",
                          hintText: "Enter your username",
                        ),
                        validator: (value) {
                          if (value!.isEmpty) {
                            return 'Please enter username';
                          }
                          return null;
                        },
                        controller: emailController,
                        keyboardType: TextInputType.name,
                      ),
                      SizedBox(
                        height: 4.h,
                      ),
                      TextFormField(
                        controller: passwordController,
                        textAlign: TextAlign.center,
                        obscureText: _obscureText,
                        validator: (value) {
                          if (value!.isEmpty) {
                            return 'Please enter password';
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
                        height: 2.h,
                      ),
                      Align(
                        alignment: Alignment.center,
                        child: RoundedButton(
                          color: Color(0xFF004AAD),
                          onPressed: () {
                            if (formGlobalKey.currentState!.validate()) {
                              formGlobalKey.currentState!.save();
                              login();
                            }
                          },
                          text: "LOG IN",
                        ),
                      ),
                      Padding(
                        padding: EdgeInsets.only(left: 2.w),
                        child: Column(
                          children: [
                            SizedBox(
                              height: 2.h,
                            ),
                            Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Text(
                                  "New to NANDI? ",
                                  style: TextStyle(fontSize: 11.sp),
                                ),
                                GestureDetector(
                                  onTap: () {
                                    Navigator.pushReplacement(
                                        context,
                                        MaterialPageRoute(
                                            builder: (context) =>
                                                SignUpPage()));
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
                          ],
                        ),
                      )
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
