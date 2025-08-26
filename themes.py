
class Themes:

    class Default:
        def buttons():
            return """QPushButton {
                        background-color: #c3af62;  
                        border-radius: 15px;
                        font-size: 20px;
                        font-weight: bold;
                        color: white;
                        padding: 12px;
                    }

                    QPushButton:hover {
                        background-color: #6d5f29;   
                    }

                    QPushButton:pressed {
                        background-color: #554b20;   
                        padding-left: 14px;          
                        padding-top: 14px;
                    }"""
        
        def menu():
            return  """
                    QMenuBar{
                    background: #c3af62;
                    border: 1px solid #8b7d4b;
                    }
                                                
                    QMenuBar:item {
                    background: transparent;
                    padding: 4px 12px;
                    }
                                                
                    QMenu{
                    background:#6d5f29;
                    padding: 4px 12px;
                    }
                                                
                    QMenu:item:selected{
                    background:#554b20;
                    }"""
                    
        def background():
            return "background: #f5f5dc"
        
        def screen():
            return """background: #d5c791;  
            color: white;
            font-size: 30px;
            font-weight: bold"""
    
    class Iris():
        def buttons():
            return """QPushButton {
                        background-color: #71557A;  
                        border-radius: 15px;
                        font-size: 20px;
                        font-weight: bold;
                        color: #fff8b4;
                        padding: 12px;
                    }

                    QPushButton:hover {
                        background-color: #614969;   
                    }

                    QPushButton:pressed {
                        background-color: #45344b;   
                        padding-left: 14px;          
                        padding-top: 14px;
                    }"""
        
        def menu():
            return  """
                    QMenuBar{
                    background: #71557A;
                    border: 1px solid #45344b;
                    }
                                                
                    QMenuBar:item {
                    background: transparent;
                    padding: 4px 12px;
                    }
                                                
                    QMenu{
                    background:#614969;
                    padding: 4px 12px;
                    }
                                                
                    QMenu:item:selected{
                    background:#45344b;
                    }"""
        
        def screen():
            return """background: #f3c8dd;  
            color: #4b1535;
            font-size: 30px;
            font-weight: bold"""
        
        def background():
            return "background: #3a345b"
    
    class Blush:
        def buttons():
            return """QPushButton {
                            background-color: #d0637c;  
                            border-radius: 15px;
                            font-size: 20px;
                            font-weight: bold;
                            color: white;
                            padding: 12px;
                        }

                        QPushButton:hover {
                            background-color: #c53f5e;   
                        }

                        QPushButton:pressed {
                            background-color: #932c44;   
                            padding-left: 14px;          
                            padding-top: 14px;
                        }"""
            
        def menu():
            return  """
                        QMenuBar{
                        background: #c53f5e;
                        border: 1px solid #932c44;
                        }
                                                    
                        QMenuBar:item {
                        background: transparent;
                        padding: 4px 12px;
                        }
                                                    
                        QMenu{
                        background:#c53f5e;
                        padding: 4px 12px;
                        }
                                                    
                        QMenu:item:selected{
                        background:#932c44;
                        }"""
                        
        def background():
            return "background: #eabec3"
            
        def screen():
            return """background: #dd868c;  
                color: #eedef3;
                font-size: 30px;
                font-weight: bold"""

    class Oracle:
        def buttons():
            return """QPushButton {
                            background-color: #4a9576;  
                            border-radius: 15px;
                            font-size: 20px;
                            font-weight: bold;
                            color: white;
                            padding: 12px;
                        }

                        QPushButton:hover {
                            background-color: #3c7960;   
                        }

                        QPushButton:pressed {
                            background-color: #2d5b48;   
                            padding-left: 14px;          
                            padding-top: 14px;
                        }"""
            
        def menu():
            return  """
                        QMenuBar{
                        background: #c65b32;
                        border: 1px solid #a34b29;
                        }
                                                    
                        QMenuBar:item {
                        background: transparent;
                        padding: 4px 12px;
                        }
                                                    
                        QMenu{
                        background:#a34b29;
                        padding: 4px 12px;
                        }
                                                    
                        QMenu:item:selected{
                        background:#8c4023;
                        }"""
                        
        def background():
            return "background: #000000"
            
        def screen():
            return """background: #e2842b;  
                color: white;
                font-size: 30px;
                font-weight: bold"""
        
    class Joker:
        def buttons():
            return """QPushButton {
                            background-color: #732424;  
                            border-radius: 15px;
                            font-size: 20px;
                            font-weight: bold;
                            color: white;
                            padding: 12px;
                        }

                        QPushButton:hover {
                            background-color: #5f1e1e;   
                        }

                        QPushButton:pressed {
                            background-color: #4c1818;   
                            padding-left: 14px;          
                            padding-top: 14px;
                        }"""
            
        def menu():
            return  """
                        QMenuBar{
                        background: #732424;
                        border: 1px solid #5f1e1e;
                        }
                                                    
                        QMenuBar:item {
                        background: transparent;
                        padding: 4px 12px;
                        }
                                                    
                        QMenu{
                        background:#5d1d1d;
                        padding: 4px 12px;
                        }
                                                    
                        QMenu:item:selected{
                        background: #491717;
                        }"""
                        
        def background():
            return "background: #000000"
            
        def screen():
            return """background: #d92323;  
                color: white;
                font-size: 30px;
                font-weight: bold"""
        
    