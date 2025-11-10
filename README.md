# EBS Volume Type Optimizer (GP3 Enforcer)

This project ensures that all new Amazon EBS volumes are created using the **GP3** volume type.  
If any volume is created with a different type (e.g., `gp2`, `io1`, `st1`, etc.), the system automatically detects it and converts the volume to **GP3**, helping reduce storage cost while maintaining performance.

---

## 🚀 How It Works

1. **EBS Volume Creation Event**
   - Whenever a new EBS volume is created, an event is published to **CloudWatch Events** (EventBridge).

2. **Event Trigger**
   - The event triggers an **AWS Lambda function**.

3. **Lambda Function Logic**
   - The Lambda function (written in Python) checks the `VolumeType` of the newly created EBS volume.
   - If the volume type is **not `gp3`**, it modifies the volume to **gp3** automatically.

---

## 🏗️ Architecture Diagram

<img width="1066" height="740" alt="image" src="https://github.com/user-attachments/assets/aad0a806-c7d1-4911-a63e-9b5600ae7984" />

📝 Documentation & Demo

📘 Standard Operating Procedure (SOP): https://www.notion.so/AWS-EBS-Optimizer-Project-2a7b7e6f248f806cab9cddd12d3a5974?source=copy_link

🎥 Demo Video: https://drive.google.com/file/d/1dpq6L9HSSDwpmas02SK-_qPucr74uhUR/view?usp=sharing

👨‍💻 Author Arfan Ahmed Cloud & DevOps Engineer
