import 'package:flutter/material.dart';
import 'package:sizer/sizer.dart';

class RoundedButton1 extends StatelessWidget {
  RoundedButton1(
      {required this.color, required this.onPressed, required this.text});
  final Color color;
  final String text;
  final onPressed;
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.symmetric(vertical: 2.w),
      child: Material(
        elevation: 1.3.w,
        color: color,
        borderRadius: BorderRadius.circular(4.8.h),
        child: MaterialButton(
          splashColor: Colors.blueGrey,
          onPressed: onPressed,
          minWidth: 46.w,
          height: 10.w,
          child: Text(
            "$text",
            style: TextStyle(
                fontSize: 14.2.sp,
                color: Colors.white,
                fontWeight: FontWeight.bold),
          ),
        ),
      ),
    );
  }
}
