%% Case 2 
% (a)
% I1 = 0.7405 A and I2 = 0.2594 A. 
% The lines intersect at maxima and minima for the cubic curve at the given input currents
% assign the fixed parameters
a = 0.5;
b = 0.1;
r = 0.1;

% Choose the value of the input current I1 < I_ext = 0.5 < I2 
I_ext = 0.5;
dt = 0.01
%% (b) and (c)

% nullclines
figure
v1 = [-1:0.1:1.5];
w1 = [-1:0.1:1.5];
v_null = (v1.*(a-v1).*(v1-1)) + I_ext;
w_null = (b/r)*v1;
p1 = plot(v1,w_null,'b','Linewidth',1.5,'HandleVisibility','off');axis([-0.6 1.5 -0.6 1.5]);hold on;
p2 = plot(w1,v_null,'r','Linewidth',1.5,'HandleVisibility','off');axis([-0.6 1.5 -0.6 1.5]);hold on;

%perturbation from fixed point
[v_phase,w_phase] = fhn(I_ext,0.55,0.55,a,b,r);
a1 = plot(v_phase,w_phase); hold on;

%limit cycle
[v_phase,w_phase] = fhn(I_ext,1,0,a,b,r);
a2 = plot(v_phase,w_phase); hold on;
legend([a1 a2],'Small perturbation from fixed point','V_0=1 | W_0=0');
hold off

figure
subplot(1,2,1)
% For v0 = 1 we plot the response versus time curves
time=0:0.05:100;
plot(time,v_phase);
hold on
ylabel({'V'});
xlabel({'time (s)'});
title({'V vs time'});

subplot(1,2,2)
plot(time,w_phase);
ylabel({'W'});
xlabel({'time (s)'});
title({'W vs time'});
