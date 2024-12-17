import 'package:flutter/material.dart';

class CurrencyCard extends StatelessWidget {
  final String name, code, amount;
  final IconData icon;
  final bool isInverted;

  const CurrencyCard({
    super.key,
    required this.name,
    required this.code,
    required this.amount,
    required this.icon,
    required this.isInverted,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      clipBehavior: Clip.hardEdge, // hard edge -> prevent overflow
      decoration: BoxDecoration(
        color: isInverted ? Colors.white : Color(0xFF2D2F32),
        borderRadius: BorderRadius.circular(25),
      ),
      child: Padding(
        padding: const EdgeInsets.all(30),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  name,
                  style: TextStyle(
                      color: isInverted ? Color(0xFF2D2F32) : Colors.white,
                      fontSize: 32,
                      fontWeight: FontWeight.w600),
                ),
                SizedBox(height: 10),
                Row(
                  children: [
                    Text(
                      amount,
                      style: TextStyle(
                          color: isInverted ? Color(0xFF2D2F32) : Colors.white,
                          fontSize: 20),
                    ),
                    SizedBox(width: 5),
                    Text(code,
                        style: TextStyle(
                            color:
                                isInverted ? Color(0xFF2D2F32) : Colors.white,
                            fontSize: 20)),
                  ],
                ),
              ],
            ),
            Transform.scale(
              scale: 2.2,
              child: Transform.translate(
                offset: Offset(-8, 15), // offset : x, y
                child: Icon(
                  icon,
                  color: isInverted ? Color(0xFF2D2F32) : Colors.white,
                  size: 88,
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
