using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add(textBox1.Text);
                listBox2.Items.Add(textBox2.Text);
                    textBox1.Text="";
                    textBox2.Text = "";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            MessageBox.Show(listBox1.SelectedItem.ToString() + "   " + listBox1.SelectedIndex.ToString());
            listBox2.Items.Add(listBox1.SelectedItem);
            listBox1.Items.Remove(listBox1.SelectedItem);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show(listBox2.SelectedItem.ToString() + "   " + listBox2.SelectedIndex.ToString());
            listBox1.Items.Add(listBox2.SelectedItem);
            listBox2.Items.Remove(listBox2.SelectedItem);
        }

      

        
    }
}
